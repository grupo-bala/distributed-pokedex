use std::{
    collections::HashMap,
    net::{SocketAddr, UdpSocket},
};

use super::{dispatcher::Dispatcher, message::Message};

pub struct Server {
    last_request: HashMap<SocketAddr, (i32, String)>,
    socket: UdpSocket,
    request_count: i32,
}

impl Server {
    pub fn new(addr: &str) -> Self {
        let socket = UdpSocket::bind(addr).expect("Não foi possível inicializar o socket UDP");

        Server {
            last_request: HashMap::new(),
            socket,
            request_count: 0,
        }
    }

    pub fn listen(&mut self) {
        loop {
            let mut buf = [0u8; 1024];

            match self.socket.recv_from(&mut buf) {
                Err(e) => println!("Falha no recebimento: {:?}", e),
                Ok((_, addr)) => {
                    self.request_count += 1;
                    self.handle_request(&addr, &String::from_utf8(buf.to_vec()).unwrap());
                }
            }
        }
    }

    fn handle_request(&mut self, addr: &SocketAddr, request: &str) {
        let request = request.split_once('\0').unwrap().0;
        let message: Message = serde_json::from_str(request).unwrap();

        if self.handle_duplicate(addr, message.id) {
            println!("[{addr:?}]: mensagem duplicada, enviando último resultado");
            self.socket
                .send_to(self.last_request.get(addr).unwrap().1.as_bytes(), addr)
                .unwrap();

            return;
        }

        let result = Dispatcher::execute(&message);
        self.last_request.insert(*addr, (message.id, result.clone()));

        if self.request_count % 2 == 0 {
            return;
        }

        self.socket.send_to(result.as_bytes(), addr).unwrap();
    }

    fn handle_duplicate(&mut self, addr: &SocketAddr, id: i32) -> bool {
        return if let Some(last_result) = self.last_request.get(addr) {
            last_result.0 == id
        } else {
            false
        };
    }
}
