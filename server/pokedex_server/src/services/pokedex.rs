use pokedex_macros::generate_skeleton;

use crate::model::{user::User, pokemon::Pokemon};

pub struct Pokedex;

#[generate_skeleton]
impl Pokedex {
    fn add_pokemon(user: User, pokemon: Pokemon) {
        println!("Usuário: {:#?}\nPokémon: {:#?}", user, pokemon);
    }
}