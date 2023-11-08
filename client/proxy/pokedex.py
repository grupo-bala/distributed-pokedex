from model.pokemon import Pokemon
from model.user import User
from network.message import Message
from network.client import Client
from proxy.id_handler import id_handler
import jsonpickle

class Pokedex:
    def add_pokemon(self, user: User, pokemon: Pokemon):
        args = jsonpickle.encode({ "user": user, "pokemon": pokemon }, unpicklable=False)
        
        data = self.__do_operation("Pokedex", "add_pokemon", args)
        
        print(data)
        
    def __do_operation(self, object_reference: str, method_id: str, args: any):
        packed_msg, msg_id = self.__pack_message(object_reference, method_id, args)
        
        client_udp = Client("127.0.0.1:9090")
        
        client_udp.send_message(packed_msg)
        
        while True:
            try:
                reply = client_udp.recieve_message()
                
                unpacked_msg: Message = self.__unpack_message(reply)
                
                if unpacked_msg.request_id == msg_id:
                    return unpacked_msg.arguments
            except TimeoutError:
                client_udp.send_message(packed_msg)

    def __pack_message(self, object_reference: str, method_id: str, args: any) -> [bytes, int]:
        msg_id = id_handler.id()
        msg = Message(0, msg_id, object_reference, method_id, args)
        
        return [jsonpickle.encode(msg, unpickable=False), msg_id]
    
    def __unpack_message(self, reply: bytes) -> Message:
        return jsonpickle.decode(reply.decode())
