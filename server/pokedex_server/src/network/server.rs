use std::{net::{UdpSocket, SocketAddr}, collections::HashMap};

use super::{message::Message, dispatcher::Dispatcher};

pub struct Server {
    last_request: HashMap<SocketAddr, i32>,
    socket: UdpSocket,
}

impl Server {
    pub fn new(addr: &str) -> Self {
        let socket = UdpSocket::bind(addr)
            .expect("Não foi possível inicializar o socket UDP");

        Server {
            last_request: HashMap::new(),
            socket
        }
    }

    pub fn listen(&mut self) {
        loop {
            let mut buf = [0u8; 1024];
            
            match self.socket.recv_from(&mut buf) {
                Err(e) => println!("Falha no recebimento: {:?}", e),
                Ok((_, addr)) => {
                    self.handle_request(
                        &addr,
                        &String::from_utf8(buf.to_vec()).unwrap()
                    );
                }
            }
        }
    }

    fn handle_request(&mut self, addr: &SocketAddr, request: &str) {
        let request = request.split_once("\0").unwrap().0;
        let message: Message = serde_json::from_str(&request).unwrap();
        
        if self.handle_duplicate(addr, message.request_id) {
            println!("Mensagem duplicada de: {addr:?}");
            return;
        }

        let result = Dispatcher::execute(&message);
        self.socket.send_to(result.as_bytes(), addr).unwrap();
    }

    fn handle_duplicate(&mut self, addr: &SocketAddr, id: i32) -> bool {
        return if let Some(_) = self.last_request.get(addr) {
            true
        } else {
            self.last_request.insert(addr.clone(), id);
            false
        }
    }
}