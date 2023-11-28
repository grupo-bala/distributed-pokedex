use std::sync::Mutex;

use lazy_static::lazy_static;
use sqlite3::Connection;

pub struct DBConnection {
    pub connection: Connection,
}

impl DBConnection {
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
        Self { connection }
    }
}

impl Default for DBConnection {
    fn default() -> Self {
        Self::new()
    }
}

lazy_static! {
    pub static ref CONNECTION: Mutex<DBConnection> = Mutex::new(DBConnection::new());
}
