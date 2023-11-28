use serde::{Deserialize, Serialize};

use super::pokemon_type::Type;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Pokemon {
    pub name: String,
    pub types: Vec<Type>,
    pub weakness: Vec<Type>,
    pub hp: i32,
    pub attack: i32,
    pub defense: i32,
    pub special_atk: i32,
    pub special_def: i32,
    pub speed: i32,
}
