use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
pub enum ResultStatus {
    Ok,
    Error
}

#[derive(Serialize, Deserialize)]
pub struct Result {
    pub status: ResultStatus,
    pub result: String
}