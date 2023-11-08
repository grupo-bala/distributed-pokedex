from services.pokedex import Pokedex
from services.authenticator import Authenticator
from model.pokemon import Pokemon
from model.user import User
from model.pokemon_type import list_types
from util import terminal
from getpass import getpass
from termcolor import cprint

pokedex = Pokedex()
auth = Authenticator()

cprint("Bem-vindo a ", end="")
cprint("Pokedex!", "red", end="\n\n")

username = input("Digite o seu nome de usuário: ")
password = getpass("Digite sua senha: ")

user = User(username, password)

terminal.clear_terminal()

print("Digite o nome do pokemon que será adicionado na ", end="")
cprint("Pokedex: ", "red", end="")

pokemon_name = input()

terminal.clear_terminal()

print("Tipos possíveis: ", end="")

list_types()

print()

pokemon_type = [
    tp
    for tp in input(f"Digite os tipos do {pokemon_name} separados por vírgula: ").split(",")
]

terminal.clear_terminal()

print("Tipos possíveis: ", end="")

list_types()

print()

weakness = [
    tp
    for tp in input(f"Digite os tipos que o {pokemon_name} é fraco contra separados por vírgula: ").split(",")
]

terminal.clear_terminal()

print("Agora digite stats do pokemon")

hp = int(input("Digite a vida do pokemon: "))
attack = int(input("Digite o ataque do pokemon: "))
defense = int(input("Digite a defesa do pokemon: "))
special_atk = int(input("Digite o dano do especial do pokemon: "))
special_def = int(input("Digite a defesa especial do pokemon: "))
speed = int(input("Digite a velocidade do pokemon: "))

pokemon = Pokemon(
    pokemon_name,
    pokemon_type,
    weakness,
    hp,
    attack,
    defense,
    special_atk,
    special_def,
    speed,
)

terminal.clear_terminal()

auth.register(user)
auth.login(user)

pokedex.add_pokemon(user, pokemon)

cprint("Pokemon adicionado", "green")
