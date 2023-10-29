from dataclasses import dataclass
from model.pokemon_type import Type

@dataclass
class Pokemon:
    name: str
    types: list[Type]
    weakness: list[Type]
    hp: int
    atk: int
    defense: int
    specialAtk: int
    specialDef: int
    speed: int