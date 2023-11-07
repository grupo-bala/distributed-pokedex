use pokedex_macros::generate_skeleton;

use crate::{model::{user::User, pokemon::Pokemon}, database::CONNECTION};

pub struct Pokedex;

#[generate_skeleton]
impl Pokedex {
    fn add_pokemon(user: User, pokemon: Pokemon) {
        let db = CONNECTION.lock().unwrap();
        let mut statement = db.connection.prepare(
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