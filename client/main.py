from services.pokedex import Pokedex
from services.authenticator import Authenticator
from model.pokemon import Pokemon
from model.user import User

pokedex = Pokedex()
auth = Authenticator()

user = User("higo", "123")
pokemon = Pokemon("Pikachu", ["ELETRIC"], ["GROUND"], 3, 4, 3, 3, 3, 6)

auth.register(user)
auth.login(user)

pokedex.add_pokemon(user, pokemon)