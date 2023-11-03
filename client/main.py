from services.pokedex import Pokedex
from model.pokemon import Pokemon
from model.user import User

pokedex = Pokedex()

user = User("ash_ketchum", "123")
pokemon = Pokemon("Pikachu", ["ELETRIC"], ["GROUND"], 3, 4, 3, 3, 3, 6)

pokedex.add_pokemon(user, pokemon)