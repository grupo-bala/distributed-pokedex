use proc_macro::TokenStream;
use quote::{quote, format_ident};
use syn::{parse_macro_input, ItemImpl, ImplItem, Type, Ident, Signature, FnArg, Pat, ItemStruct};

mod data;
mod util;

use data::DispatcherArgs;

use crate::util::format_camel_case;

#[proc_macro_attribute]
pub fn generate_dispatcher(_attrs: TokenStream, tokens: TokenStream) -> TokenStream {
    let parsed = parse_macro_input!(tokens as ItemStruct);
    let attrs = parse_macro_input!(_attrs as DispatcherArgs);
    let struct_name = &parsed.ident;

    let braces = attrs.structs.iter().map(|ident| {
        let skeleton = format_ident!("{}Skeleton", ident);

        quote! {
            stringify!(#ident) => #skeleton::execute(&msg.method_id, &msg.arguments)
        }
    });

    let dispatcher = quote! {
        #parsed

        impl #struct_name {
            pub fn execute(msg: &Message) -> String {
                let output = match msg.object_reference.as_str() {
                    #(#braces),*,
                    _ => panic!("Object does not exists")
                };

                let result = match output {
                    Ok(res) => Result {
                        status: ResultStatus::Ok,
                        result: res
                    },
                    Err(e) => Result {
                        status: ResultStatus::Error,
                        result: e
                    }
                };

                let response = Message {
                    msg_type: 1,
                    id: msg.id,
                    object_reference: msg.object_reference.clone(),
                    method_id: msg.method_id.clone(),
                    arguments: serde_json::to_string(&result).unwrap(),
                };

                serde_json::to_string(&response).unwrap()
            }
        }
    };
    
    TokenStream::from(dispatcher)
}

#[proc_macro_attribute]
pub fn generate_skeleton(_attrs: TokenStream, tokens: TokenStream) -> TokenStream {
    let parsed = parse_macro_input!(tokens as ItemImpl);
    let struct_ident = if let Type::Path(p) = parsed.self_ty.as_ref() {
        &p.path.segments.last().unwrap().ident
    } else {
        unreachable!()
    };
    
    let fns: Vec<_> = parsed.items.iter().filter_map(|item| {
        if let ImplItem::Fn(f) = item {
            Some(&f.sig)
        } else {
            None
        }
    }).collect();

    let skeleton = generate_skeleton_impl(&parsed, struct_ident, &fns);
    let args_structs = generate_args_structs(&fns);

    let definitions = quote! {
        #skeleton

        #args_structs
    };

    TokenStream::from(definitions)
}

fn generate_execute_method(fns: &Vec<&Signature>) -> proc_macro2::TokenStream {
    let execute_implementations = fns.iter().map(|sig| {
        let ident = &sig.ident;

        quote! {
            stringify!(#ident) => Self::#ident(args)
        }
    });

    let execute_method = quote! {
        pub fn execute(method: &str, args: &str) -> Result<String, String> {
            match method {
                #(#execute_implementations),*,
                _ => panic!("Method does not exists")
            }
        }
    };

    execute_method
}

fn generate_skeleton_impl(
    input: &ItemImpl, struct_ident: &Ident, fns: &Vec<&Signature>
) -> proc_macro2::TokenStream {
    let execute_method = generate_execute_method(&fns);
    let skeleton_methods = fns.iter().map(|sig| {
        let ident = &sig.ident;
        let camel_case_ident = format_camel_case(&ident.to_string());
        let input_struct_ident = format_ident!("Input{}", camel_case_ident);
        let args = sig.inputs.iter().filter_map(|input| {
            if let FnArg::Typed(arg) = input {
                if let Pat::Ident(name) = arg.pat.as_ref() {
                    Some(&name.ident)
                } else {
                    None
                }
            } else {
                None
            }
        });

        quote! {
            pub fn #ident(args: &str) -> Result<String, String> {
                let args: #input_struct_ident = serde_json::from_str(args).unwrap();
                let output = #struct_ident::#ident(#(args.#args),*)
                    .map(|res| serde_json::to_string(&res).unwrap());

                return output;
            }
        }
    });

    let skeleton_ident = format_ident!("{}Skeleton", struct_ident);
    let definition = quote! {
        #input

        pub struct #skeleton_ident;

        impl #skeleton_ident {
            #(#skeleton_methods)*

            #execute_method
        }
    };

    definition
}

fn generate_args_structs(fns: &Vec<&Signature>) -> proc_macro2::TokenStream {
    let structs = fns.iter().map(|f| {
        let args = f.inputs.iter().filter_map(|arg| {
            if let FnArg::Typed(arg) = arg {
                Some(arg)
            } else {
                None
            }
        });

        let camel_case_ident = format_camel_case(&f.ident.to_string());
        let struct_name = format_ident!("Input{}", camel_case_ident);

        quote! {
            #[derive(serde::Serialize, serde::Deserialize)]
            struct #struct_name {
                #(#args),*
            }
        }
    });

    let definitions = quote! {
        #(#structs)*
    };

    definitions
}