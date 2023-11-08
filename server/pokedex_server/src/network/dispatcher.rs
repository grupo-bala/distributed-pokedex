use pokedex_macros::generate_dispatcher;
use crate::{services::{pokedex::PokedexSkeleton, authenticator::AuthenticatorSkeleton}, network::{message::Message, result::{Result, ResultStatus}}};

#[generate_dispatcher(Pokedex, Authenticator)]
pub struct Dispatcher;