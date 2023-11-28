use syn::{parse::Parse, Ident, Token};

#[derive(Debug)]
pub struct DispatcherArgs {
    pub structs: Vec<Ident>,
}

impl Parse for DispatcherArgs {
    fn parse(input: syn::parse::ParseStream) -> syn::Result<Self> {
        let mut idents = Vec::new();

        loop {
            if input.is_empty() {
                break;
            }

            idents.push(input.parse::<Ident>().unwrap());

            if input.is_empty() {
                break;
            }

            input.parse::<Token![,]>()?;
        }

        Ok(DispatcherArgs { structs: idents })
    }
}
