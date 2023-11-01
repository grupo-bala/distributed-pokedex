use std::net::UdpSocket;

use super::message::Message;

pub struct Server {
    socket: UdpSocket,
}

impl Server {
    pub fn new(addr: &str) -> Self {
        let socket = UdpSocket::bind(addr)
            .expect("Não foi possível inicializar o socket UDP");

        Server { socket }
    }

    pub fn listen(&mut self) {
        let mut buf = [0u8; 1024];

        loop {
            if let Err(e) = self.socket.recv(&mut buf) {
                println!("Falha no recebimento: {:?}", e);
            }

            Self::handle_request(&String::from_utf8(buf.to_vec()).unwrap());
        }
    }

    fn handle_request(request: &str) {
        let request = request.split_once("\0").unwrap().0;
        let message: Message = serde_json::from_str(&request).unwrap();

        println!("{:#?}", message);
    }
}