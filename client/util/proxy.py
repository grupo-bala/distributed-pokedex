from util.singleton import SingletonMeta
from util.id_handler import id_handler
from network.message import Message
from network.client import client
from network.result import Result
import jsonpickle

class Proxy(metaclass=SingletonMeta):
    def do_operation(self, object_reference: str, method_id: str, args: dict) -> dict:
        encoded_args = jsonpickle.encode(args, unpicklable=False)
        packed_msg, msg_id = self.__pack_message(object_reference, method_id, encoded_args)
        
        client.send_message(packed_msg)
        
        while True:
            try:
                reply = client.receive_message()
                unpacked_msg: Message = self.__unpack_message(reply)

                if unpacked_msg.id != msg_id:
                    continue

                result: Result = Result(**jsonpickle.decode(unpacked_msg.arguments))

                if result.status == "Error":
                    raise Exception(result.result)

                return jsonpickle.decode(result.result)
            except TimeoutError:
                client.send_message(packed_msg)
    
    def __pack_message(self, object_reference: str, method_id: str, args: str) -> [str, int]:
        msg_id = id_handler.id()
        msg = Message(msg_id, 0, object_reference, method_id, args)
        
        return [jsonpickle.encode(msg, unpicklable=False), msg_id]
    
    def __unpack_message(self, reply: bytes) -> Message:
        return Message(**jsonpickle.decode(reply.decode()))
    
proxy = Proxy()