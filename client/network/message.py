from dataclasses import dataclass

@dataclass
class Message:
    id: int
    msg_type: int
    object_reference: str
    method_id: str
    arguments: str