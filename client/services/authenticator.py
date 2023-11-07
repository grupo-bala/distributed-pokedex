from model.user import User
from network.message import Message
from network.client import Client
from services.id_handler import id_handler
import jsonpickle

class Authenticator:
    def login(self, user: User):
        args = jsonpickle.encode({ "user": user }, unpicklable=False)
        msg = Message(0, id_handler.id(), "Authenticator", "login", args)
        json: str = jsonpickle.encode(msg, unpicklable=False)

        data = jsonpickle.decode(Client("127.0.0.1:9090").send_message(json).decode())
        print(data)
    
    def register(self, user: User):
        args = jsonpickle.encode({ "user": user }, unpicklable=False)
        msg = Message(0, id_handler.id(), "Authenticator", "register", args)
        json: str = jsonpickle.encode(msg, unpicklable=False)

        data = jsonpickle.decode(Client("127.0.0.1:9090").send_message(json).decode())
        print(data)