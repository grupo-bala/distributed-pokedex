from dataclasses import dataclass
from model.pokemon_type import Type, color_type
from termcolor import colored

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
    
    def __str__(self) -> str:
        bold_text = lambda x: colored(x, attrs=['bold'])
        
        header = f"\n{bold_text(self.name.upper())} [{', '.join(map(lambda x: colored(x.lower(), *color_type(x)), self.types))}]"
        
        stats = f"""
HP............{bold_text(self.hp)}
Attack........{bold_text(self.attack)}
Defense.......{bold_text(self.defense)}
Sp. Attack....{bold_text(self.special_atk)}
Sp. Defense...{bold_text(self.special_def)}
Speed.........{bold_text(self.speed)}"""

        weakness = f"\nWeakness......{', '.join(map(lambda x: colored(x.lower(), *color_type(x)), self.weakness))}"

        return header + stats + weakness