use std::sync::Mutex;

use lazy_static::lazy_static;
use sqlite3::Connection;

use crate::model::{user::User, pokemon::Pokemon};

pub struct Database {
    connection: Connection
}

impl Database {
    pub fn new() -> Self {
        let connection = sqlite3::open("db.sqlite").unwrap();
        let setup_tables = "
            PRAGMA foreign_keys = ON;

            CREATE TABLE IF NOT EXISTS user (
                username text primary key,
                password text
            );

            CREATE TABLE IF NOT EXISTS pokemon (
                id integer PRIMARY key,
                name text,
                types text,
                weakness text,
                hp integer,
                attack integer,
                defense integer,
                special_atk integer,
                special_def integer,
                speed integer,
                user_username text,
  	            FOREIGN key (user_username) REFERENCES user(username)
           ); 
        ";

        connection.execute(setup_tables).unwrap();
        Database { connection }
    }

    pub fn add_pokemon(&mut self, user: User, pokemon: Pokemon) {
        let mut statement = self.connection.prepare(
            "INSERT INTO pokemon (name, types, weakness, hp, attack, defense, special_atk, special_def, speed, user_username) VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            );"
        ).unwrap();

        let types = pokemon.types
            .iter()
            .map(|t| { t.to_string() })
            .collect::<Vec<_>>()
            .join(", ");

        let weakness = pokemon.weakness
            .iter()
            .map(|t| { t.to_string() })
            .collect::<Vec<_>>()
            .join(", ");

        statement.bind(1, pokemon.name.as_str()).unwrap();
        statement.bind(2, types.as_str()).unwrap();
        statement.bind(3, weakness.as_str()).unwrap();
        statement.bind(4, pokemon.hp as i64).unwrap();
        statement.bind(5, pokemon.attack as i64).unwrap();
        statement.bind(6, pokemon.defense as i64).unwrap();
        statement.bind(7, pokemon.special_atk as i64).unwrap();
        statement.bind(8, pokemon.special_def as i64).unwrap();
        statement.bind(9, pokemon.speed as i64).unwrap();
        statement.bind(10, user.username.as_str()).unwrap();

        statement.next().unwrap();
    }
}

lazy_static! {
    pub static ref DATABASE: Mutex<Database> = Mutex::new(Database::new());
}