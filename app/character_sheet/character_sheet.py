from .character_classes import CharacterClass

class CharacterSheet:
    
    name: str
    player_class: CharacterClass
    race: str
    background: str
    level: int = 1