use pokedex_macros::generate_skeleton;

use crate::{model::{user::User, pokemon::Pokemon}, database::DATABASE};

pub struct Pokedex;

#[generate_skeleton]
impl Pokedex {
    fn add_pokemon(user: User, pokemon: Pokemon) {
        let mut db = DATABASE.lock().unwrap();
        db.add_pokemon(&user, &pokemon);
    }
}