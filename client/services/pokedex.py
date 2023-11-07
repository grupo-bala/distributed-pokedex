from model.pokemon import Pokemon
from model.user import User
from network.message import Message
from network.client import Client
import jsonpickle

class Pokedex:
    def __init__(self) -> None:
        self.next_id = 0

    def add_pokemon(self, user: User, pokemon: Pokemon):
        args = jsonpickle.encode({ "user": user, "pokemon": pokemon }, unpicklable=False)
        msg = Message(0, self.next_id, "Pokedex", "add_pokemon", args)
        json: str = jsonpickle.encode(msg, unpicklable=False)

        self.next_id += 1

        data = jsonpickle.decode(Client("127.0.0.1:9090").send_message(json).decode())
        print(data)

