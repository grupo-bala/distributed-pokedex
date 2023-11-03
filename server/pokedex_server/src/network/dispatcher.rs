use pokedex_macros::generate_dispatcher;
use crate::services::pokedex::PokedexSkeleton;

#[generate_dispatcher(Pokedex)]
pub struct Dispatcher;