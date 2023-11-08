from typing import Literal, get_args

Type = Literal[
    "NORMAL",
    "FIRE",
    "WATER",
    "GRASS",
    "ELETRIC",
    "ICE",
    "FIGHTING",
    "POISON",
    "GROUND",
    "FLYING",
    "PSYCHIC",
    "BUG",
    "ROCK",
    "GHOST",
    "DRAGON",
    "DARK",
    "STEEL",
    "FAIRY",
]


def list_types():
    for (i, tp) in enumerate(get_args(Type)):
        print(f"{tp}", end="" if i == 0 else " ")
