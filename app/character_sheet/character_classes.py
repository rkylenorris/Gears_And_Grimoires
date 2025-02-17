from dataclasses import dataclass

@dataclass
class HitPoints:
    max_hp: int
    current_hp: int
    temp_hp: int = 0

class AbilityScores:
    might: int
    reflexes: int
    endurance_core: int
    arcane_logic: int
    aether_sense: int
    presence: int
    
    def __init__(self, starting_scores: dict[str, int]):
        self.might = starting_scores.get('might', 0)
        self.reflexes = starting_scores.get('reflexes', 0)
        self.endurance_core = starting_scores.get('endurance_core', 0)
        self.arcane_logic = starting_scores.get('arcane_logic', 0)
        self.aether_sense = starting_scores.get('aether_sense', 0)
        self.presence = starting_scores.get('presence', 0)

    



class Proficencies:
    def __init__(self, armor: list[str], weapons: list[str], tools: list[str]):
        self.armor = armor
        self.weapons = weapons
        self.tools = tools
        

class Equipment:
    def __init__(self, armor: dict[str, int], weapons: dict[str, int], tools: dict[str, str],
                 potions: dict[str, int], currency: dict[str, int], misc):
        self.armor = armor
        self.weapons = weapons
        self.tools = tools
        self.potions = potions
        self.currency = currency
        self.misc = misc



class CharacterClass:
    def __init__(self, name: str, hit_die: str, primary_abilities: list[str], saving_throws,
                 proficiencies : Proficencies, skills, starting_equipment: Equipment,
                 starting_ability_scores: dict[str, int]):
        self.name = name
        self.hit_die = hit_die
        self.primary_abilities = primary_abilities
        self.saving_throws = saving_throws
        self.proficiencies  = proficiencies 
        self.skills = skills
        self.starting_equipment = starting_equipment
        self.starting_ability_scores = starting_ability_scores


class Race:
    def __init__(self, name, ability_bonuses, size, speed, languages, traits):
        self.name = name
        self.ability_bonuses = ability_bonuses
        self.size = size
        self.speed = speed
        self.languages = languages
        self.traits = traits
        
        
class Background:
    def __init__(self, name, desc, skill_proficiencies, tool_proficiencies, languages, equipment, feature, trait):
        self.name = name
        self.description = desc
        self.skill_proficiencies = skill_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.languages = languages
        self.equipment = equipment
        self.feature = feature