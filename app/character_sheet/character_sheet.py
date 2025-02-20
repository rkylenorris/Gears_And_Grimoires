from .character_classes import CharacterClass, Race, Background, Equipment, Proficencies, AbilityScores, HitPoints

class CharacterSheet:
    
    name: str
    level: int = 1
    player_class: CharacterClass
    race: Race
    background: Background
    abilities: AbilityScores
    equipment: Equipment
    proficencies: Proficencies
    armor_class: int
    initiative: int
    hit_points: HitPoints
    appearance: str
    
    def __init__(self, name: str, player_class: CharacterClass, race: Race,
                 background: Background, appearance: str):
        self.name = name
        self.player_class = player_class
        self.race = race
        self.background = background
        self.abilities = AbilityScores(starting_scores=player_class.starting_ability_scores)
        # self.equipment = equipment
        # self.proficencies = proficencies
        # self.armor_class = armor_class
        self.hit_points = HitPoints()
        self.hit_points.roll_hit_points(player_class.hit_die, self.abilities.endurance_core)
        self.appearance = appearance
    
    