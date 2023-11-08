from model.pokemon import Pokemon
from model.user import User
from network.message import Message
from network.client import Client
from proxy.id_handler import id_handler
import jsonpickle

class Pokedex:
    def add_pokemon(self, user: User, pokemon: Pokemon):
        args = jsonpickle.encode({ "user": user, "pokemon": pokemon }, unpicklable=False)
        msg = Message(0, id_handler.id(), "Pokedex", "add_pokemon", args)
        json: str = jsonpickle.encode(msg, unpicklable=False)

        data = jsonpickle.decode(Client("127.0.0.1:9090").send_message(json).decode())
        print(data)
