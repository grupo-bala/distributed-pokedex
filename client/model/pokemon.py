from dataclasses import dataclass
from model.pokemon_type import Type

@dataclass
class Pokemon:
    name: str
    types: list[Type]
    weakness: list[Type]
    hp: int
    attack: int
    defense: int
    special_atk: int
    special_def: int
    speed: int