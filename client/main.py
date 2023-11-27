from services.pokedex import Pokedex
from services.authenticator import Authenticator
from model.pokemon import Pokemon
from model.user import User
from model.pokemon_type import list_types, get_types
from util import terminal
from getpass import getpass
from termcolor import cprint

pokedex = Pokedex()
auth = Authenticator()

cprint("Bem-vindo a ", end="")
cprint("Pokedex!", "red", end="\n\n")

input("Pressione enter para continuar...")

terminal.clear_terminal()

user = None

def login():
    print("Credeciais para o login...")

    username = input("Digite o seu nome de usuário: ")
    password = getpass("Digite sua senha: ")

    global user

    user = User(username, password)

    try:
        terminal.clear_terminal()

        auth.login(user)

        cprint("Login realizado com sucesso!\n", "green")

        input("Pressione enter para continuar...")

        terminal.clear_terminal()

        return True
    except Exception as e:
        terminal.clear_terminal()

        cprint(f"{str(e)}\nTente novamente!\n", "red")

        input("Pressione enter para continuar...")

        return False

def register():
    print("Credencais para o registro...")

    username = input("Digite o seu nome de usuário: ")
    password = getpass("Digite sua senha: ")

    global user

    user = User(username, password)

    try:
        auth.register(user)
        auth.login(user)

        terminal.clear_terminal()

        cprint("Registro realizado com sucesso!\n", "green")

        input("Pressione enter para continuar...")

        terminal.clear_terminal()

        return True
    except Exception as e:
        terminal.clear_terminal()

        cprint(f"{str(e)}\nTente novamente!\n", "red")

        input("Pressione enter para continuar...")

        return False

while True:
    option = input("Deseja fazer login ou registrar(login/registrar)? ").lower()

    if option == "":
        terminal.clear_terminal()

        continue

    terminal.clear_terminal()

    if option == "login" and login():
        break
    elif option == "registrar" and register():
        break
    elif option != "login" and option != "registrar":
        terminal.clear_terminal()

        cprint("Opção inválida!\n", "red")
        
        input("As opções são login ou registrar! Pressione enter para continuar...")

    terminal.clear_terminal()

def add_pokemon():
    print("Digite o nome do pokemon que será adicionado na ", end="")
    cprint("Pokedex: ", "red", end="")

    pokemon_name = input().lower()

    terminal.clear_terminal()

    print("Tipos possíveis: ", end="")

    list_types()

    print()

    pokemon_type = []

    while True:
        pokemon_type = [
            tp.upper()
            for tp in input(f"Digite os tipos do {pokemon_name} separados por vírgula: ").split(",")
        ]

        has_invalid_type = False

        for type in pokemon_type:
            if type not in get_types():
                has_invalid_type = True

                terminal.clear_terminal()

                cprint("Tipo inválido, tente novamente!\n\n", "red")

                input("Pressione enter para continuar...")

                terminal.clear_terminal()

                break
        
        if not has_invalid_type:
            break

    terminal.clear_terminal()

    print("Tipos possíveis: ", end="")

    list_types()

    print()

    weakness = []

    while True:
        weakness = [
            tp.upper()
            for tp in input(f"Digite os tipos que o {pokemon_name} é fraco contra separados por vírgula: ").split(",")
        ]

        has_invalid_type = False

        for type in pokemon_type:
            if type not in get_types():
                has_invalid_type = True

                terminal.clear_terminal()

                cprint("Tipo inválido, tente novamente!\n\n", "red")

                input("Pressione enter para continuar...")

                terminal.clear_terminal()

                break
        
        if not has_invalid_type:
            break

    terminal.clear_terminal()

    print("Agora digite os stats do pokemon")

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

    try:
        pokedex.add_pokemon(user, pokemon)

        cprint("Pokemon adicionado!", "green")

        input("Pressione enter para continuar...")
    except Exception as e:
        cprint(f"{str(e)}\n", "red")

        input("Pressione enter para continuar...")


def remove_pokemon():
    pokemon_name = input("Nome do pokemon(deve ser o exato nome): ").lower()

    terminal.clear_terminal()

    try:
        pokedex.remove_pokemon(user, pokemon_name)

        cprint("Pokemon removido!", "green")
    except Exception as e:
        cprint(f"{str(e)}\n\n", "red")

    input("Pressione enter para continuar...")

    terminal.clear_terminal()

def search_pokemon():
    terminal.clear_terminal()

    pokemon_name = input("Busca: ").lower()

    terminal.clear_terminal()

    try:
        pokemons = pokedex.search_pokemon(user, pokemon_name)

        if len(pokemons) == 0:
            cprint("Nenhum pokemon encontrado!", "red")
        else:
            terminal.print_pokemons(2, pokemons)
    except Exception as e:
        cprint(f"{str(e)}\n\n", "red")

    input("Pressione enter para continuar...")
    
    terminal.clear_terminal()


while True:
    option = input("Qual o comando que deseja executar(adicionar/remover/buscar/sair)? ").lower()

    if option == "adicionar":
        add_pokemon()
    elif option == "remover":
        remove_pokemon()
    elif option == "buscar":
        search_pokemon()
    elif option == "sair":
        break
    else:
        terminal.clear_terminal()
        cprint("Opção inválida!\n\n", "red")
        
        input("As opções válidas são adicionar, remover, buscar ou sair! Pressione enter para continuar...")

    terminal.clear_terminal()

terminal.clear_terminal()