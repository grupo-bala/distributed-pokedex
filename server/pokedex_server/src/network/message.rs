use serde::{Serialize, Deserialize};

#[derive(Debug, Serialize, Deserialize)]
pub struct Message {
    pub msg_type: i32,
    pub request_id: i32,
    pub object_reference: String,
    pub method_id: String,
    pub arguments: String
}