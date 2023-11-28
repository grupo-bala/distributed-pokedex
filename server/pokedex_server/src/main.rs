use std::env;

use pokedex_server::network::server::Server;

fn main() {
    let is_error_env = env::args().any(|arg| arg == "--error");

    let mut server = Server::new("127.0.0.1:9090", is_error_env);
    server.listen();
}
