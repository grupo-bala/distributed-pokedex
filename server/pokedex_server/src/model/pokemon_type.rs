use derive_more::Display;
use serde::{Serialize, Deserialize};

#[derive(Debug, Display, Serialize, Deserialize)]
pub enum Type {
    NORMAL,
    FIRE,
    WATER,
    GRASS,
    ELETRIC,
    ICE,
    FIGHTING,
    POISON,
    GROUND,
    FLYING,
    PSYCHIC,
    BUG,
    ROCK,
    GHOST,
    DRAGON,
    DARK,
    STEEL,
    FAIRY,
}