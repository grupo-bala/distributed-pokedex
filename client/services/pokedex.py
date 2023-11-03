from model.pokemon import Pokemon
from model.user import User
from network.message import Message
from network.client import Client
import jsonpickle

class Pokedex:
    def add_pokemon(self, user: User, pokemon: Pokemon):
        args = jsonpickle.encode({ "user": user, "pokemon": pokemon }, unpicklable=False)
        msg = Message(0, 90, "Pokedex", "add_pokemon", args)
        json: str = jsonpickle.encode(msg, unpicklable=False)

        Client("127.0.0.1:9090").send_message(json)
