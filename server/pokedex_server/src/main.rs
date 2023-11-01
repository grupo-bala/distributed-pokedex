use pokedex_server::network::server::Server;

fn main() {
    let mut server = Server::new("127.0.0.1:8765");
    server.listen();
}
