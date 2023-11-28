use derive_more::Display;
use serde::{Deserialize, Serialize};
use strum::EnumString;

#[derive(Debug, Clone, Display, Serialize, Deserialize, EnumString)]
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
