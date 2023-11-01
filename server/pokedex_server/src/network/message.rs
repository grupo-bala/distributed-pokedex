use serde::{Serialize, Deserialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct Message {
    msg_type: i32,
    request_id: i32,
    object_reference: String,
    method_id: String,
    arguments: String
}