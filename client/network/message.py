from dataclasses import dataclass

@dataclass
class Message:
    msg_type: int
    request_id: int
    object_reference: str
    method_id: str
    arguments: str