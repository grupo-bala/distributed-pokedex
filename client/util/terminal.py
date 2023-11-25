import os
from termcolor import colored
from model.pokemon import Pokemon
from typing import TypeVar

def clear_terminal():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def print_pokemons(cols: int, pokemons: list[Pokemon]):
    if not pokemons:
        print(colored("Nenhum pokemon com esse nome foi encontrado :(", attrs=['bold']))
        return
    
    pokemon_data = split_by_n(cols, [str(pokemon).split("\n") for pokemon in pokemons])
    out = ""
    
    for line in pokemon_data:
        for info_index in range(len(line[0])):
            for pokemon in line:
                out += pokemon[info_index] + " \t" * 2
                
            out += "\n"
    
    print(out)

T = TypeVar("T")

def split_by_n(n: int, array: list[T]) -> list[T]:
    out = []
    
    for i in range(0, len(array), n):
        out.append(array[i:i + n])
    
    return out