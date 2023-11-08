from util.singleton import SingletonMeta
from client.util.id_handler import id_handler
from network.message import Message
from network.client import client
import jsonpickle

class Proxy(metaclass=SingletonMeta):
    def do_operation(self, object_reference: str, method_id: str, args: str) -> str:
        packed_msg, msg_id = self.__pack_message(object_reference, method_id, args)
        
        client.send_message(packed_msg)
        
        while True:
            try:
                reply = client.recieve_message()
                
                unpacked_msg: Message = self.__unpack_message(reply)
                
                if unpacked_msg.request_id == msg_id:
                    return unpacked_msg.arguments
            except TimeoutError:
                client.send_message(packed_msg)
    
    def __pack_message(self, object_reference: str, method_id: str, args: str) -> [str, int]:
        msg_id = id_handler.id()
        msg = Message(0, msg_id, object_reference, method_id, args)
        
        return [jsonpickle.encode(msg, unpickable=False), msg_id]
    
    def __unpack_message(self, reply: bytes) -> Message:
        return jsonpickle.decode(reply.decode())
    
proxy = Proxy()