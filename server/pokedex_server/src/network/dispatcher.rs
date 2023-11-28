use crate::{
    network::{
        message::Message,
        result::{Result, ResultStatus},
    },
    services::{authenticator::AuthenticatorSkeleton, pokedex::PokedexSkeleton},
};
use pokedex_macros::generate_dispatcher;

#[generate_dispatcher(Pokedex, Authenticator)]
pub struct Dispatcher;
