from model.pokemon import Pokemon
from model.user import User
import jsonpickle

pikachu = Pokemon("Pikachu", ["ELETRIC"], ["WATER"], 2, 4, 3, 4, 3, 4)
user = User("ash", "123")

print(jsonpickle.encode(pikachu, unpicklable=False))
print(jsonpickle.encode(user, unpicklable=False))