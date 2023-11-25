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

def color_type(type: Type) -> tuple[str]:
        color: tuple[str] = ()
        
        match type:
            case "FIRE": color = ("light_red",)
            case "WATER": color = ("blue",)
            case "GRASS": color = ("light_green",)
            case "ELETRIC": color = ("light_yellow",)
            case "ICE": color = ("light_blue",)
            case "FIGHTING": color = ("red",)
            case "POISON": color = ("magenta",)
            case "GROUND": color = ("yellow",)
            case "FLYING": color = ("light_blue",)
            case "PSYCHIC": color = ("light_magenta",)
            case "BUG": color = ("cyan",)
            case "ROCK": color = ("grey",)
            case "GHOST": color = ("light_grey",)
            case "DRAGON": color = ("red",)
            case "DARK": color = ("grey", "on_black")
            case "STEEL": color = ("light_grey",)
            case "FAIRY": color = ("magenta",)
            case _: color = ("white",)
        
        return color

def list_types():
    for (i, tp) in enumerate(get_args(Type)):
        print(f"{tp}", end="" if i == 0 else " ")
