use pokedex_macros::generate_skeleton;
use sqlite3::State;

use crate::{database::CONNECTION, model::user::User};

pub struct Authenticator;

#[generate_skeleton]
impl Authenticator {
    pub fn register(user: User) -> Result<(), String> {
        println!("[{}]: register()", user.username);

        let db = CONNECTION.lock().unwrap();
        let mut statement = db
            .connection
            .prepare("INSERT INTO user VALUES (?, ?);")
            .unwrap();

        statement.bind(1, user.username.as_str()).unwrap();
        statement.bind(2, user.password.as_str()).unwrap();

        if statement.next().is_err() {
            return Err("Nome de usuário já existe".to_string());
        }

        Ok(())
    }

    pub fn login(user: User) -> Result<(), String> {
        println!("[{}]: login()", user.username);

        let db = CONNECTION.lock().unwrap();
        let mut statement = db
            .connection
            .prepare("SELECT * FROM user WHERE username = ? AND password = ?;")
            .unwrap();

        statement.bind(1, user.username.as_str()).unwrap();
        statement.bind(2, user.password.as_str()).unwrap();

        if let State::Row = statement.next().unwrap() {
            Ok(())
        } else {
            Err("Credenciais inválidas".to_string())
        }
    }
}
