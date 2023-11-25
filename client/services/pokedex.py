from model.pokemon import Pokemon
from model.user import User
from util.proxy import proxy

class Pokedex:
    def add_pokemon(self, user: User, pokemon: Pokemon):
        proxy.do_operation("Pokedex", "add_pokemon", { "user": user, "pokemon": pokemon })
        
    def search_pokemon(self, user: User, pokemon_name: str): 
        result = proxy.do_operation("Pokedex", "search_pokemon", { "user": user, "name": pokemon_name })
        
        if not result:
            return []
        
        return [Pokemon(**pokemon) for pokemon in result]