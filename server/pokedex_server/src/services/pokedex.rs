use std::str::FromStr;

use pokedex_macros::generate_skeleton;
use sqlite3::State;

use crate::{model::{user::User, pokemon::Pokemon, pokemon_type::Type}, database::CONNECTION};

use super::authenticator::Authenticator;

pub struct Pokedex;

#[generate_skeleton]
impl Pokedex {
    pub fn add_pokemon(user: User, pokemon: Pokemon) -> Result<(), String> {
        let found_pokemons = Self::search_pokemon(user.clone(), pokemon.name.clone())?;

        if !found_pokemons.is_empty() {
            return Err("Pokémon já existe na pokédex".to_string());
        }

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
        Ok(())
    }

    pub fn search_pokemon(user: User, name: String) -> Result<Vec<Pokemon>, String> {
        Authenticator::login(user.clone())?;

        let db = CONNECTION.lock().unwrap();

        let mut statement = db.connection.prepare(
            "SELECT * FROM pokemon 
            WHERE pokemon.user_username = ?
            AND UPPER(pokemon.name) LIKE UPPER(?);"
        ).unwrap();

        statement.bind(1, user.username.as_str()).unwrap();
        statement.bind(2, format!("%{name}%").as_str()).unwrap();

        let mut pokemons = Vec::new();
        while let State::Row = statement.next().unwrap() {
            let pokemon = Pokemon {
                name: statement.read(1).unwrap(),
                types: statement.read::<String>(2)
                    .unwrap()
                    .split(", ")
                    .map(|t| { Type::from_str(t).unwrap() })
                    .collect(),
                weakness: statement.read::<String>(3)
                    .unwrap()
                    .split(", ")
                    .map(|w| { Type::from_str(w).unwrap() })
                    .collect(),
                hp: statement.read::<i64>(4).unwrap() as i32,
                attack: statement.read::<i64>(5).unwrap() as i32,
                defense: statement.read::<i64>(6).unwrap() as i32,
                special_atk: statement.read::<i64>(7).unwrap() as i32,
                special_def: statement.read::<i64>(8).unwrap() as i32,
                speed: statement.read::<i64>(9).unwrap() as i32
            };

            pokemons.push(pokemon);
        }

        Ok(pokemons)
    }

    fn remove_pokemon(user: User, name: String) -> Result<(), String> {
        let found_pokemons = Self::search_pokemon(user.clone(), name.clone())?;

        if found_pokemons.is_empty() {
            return Err("Pokémon não existe".to_string())
        }

        let db = CONNECTION.lock().unwrap();
        let mut statement = db.connection.prepare(
            "DELETE FROM pokemon WHERE pokemon.user_username = ? AND pokemon.name = ?;"
        ).unwrap();

        statement.bind(1, user.username.as_str()).unwrap();
        statement.bind(2, name.as_str()).unwrap();

        statement.next().unwrap();
        Ok(())
    }
}