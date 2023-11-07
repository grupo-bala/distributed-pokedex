use pokedex_macros::generate_dispatcher;
use crate::services::{pokedex::PokedexSkeleton, authenticator::AuthenticatorSkeleton};

#[generate_dispatcher(Pokedex, Authenticator)]
pub struct Dispatcher;