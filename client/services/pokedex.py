from model.pokemon import Pokemon
from model.user import User
from client.util.proxy import proxy
import jsonpickle

class Pokedex:
    def add_pokemon(self, user: User, pokemon: Pokemon):
        args = jsonpickle.encode({ "user": user, "pokemon": pokemon }, unpicklable=False)
        
        data = proxy.do_operation("Pokedex", "add_pokemon", args)
        
        print(data)