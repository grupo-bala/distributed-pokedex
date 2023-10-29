use pokedex_server::model::{pokemon::Pokemon, pokemon_type::Type, user::User};

fn main() {
    let charmander = Pokemon {
        name: "Charmander".to_string(),
        types: vec![Type::FIRE],
        weakness: vec![Type::WATER, Type::GROUND, Type::ROCK],
        hp: 3,
        atk: 4,
        def: 3,
        special_atk: 4,
        special_def: 3,
        speed: 4
    };

    let user = User {
        username: "ash".to_string(),
        password: "123".to_string()
    };

    println!("{}", serde_json::to_string(&charmander).unwrap());
    println!("{}", serde_json::to_string(&user).unwrap());
}
