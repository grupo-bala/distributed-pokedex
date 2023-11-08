from model.pokemon import Pokemon
from model.user import User
from util.proxy import proxy

class Pokedex:
    def add_pokemon(self, user: User, pokemon: Pokemon):
        proxy.do_operation("Pokedex", "add_pokemon", { "user": user, "pokemon": pokemon })
        