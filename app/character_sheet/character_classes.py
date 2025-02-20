from dataclasses import dataclass
from typing import Union
from random import randint
import json
from pathlib import Path

@dataclass
class HitPoints:
    max_hp: int = 0
    current_hp: int
    temp_hp: int = 0
    
    def roll_hit_points(self, hit_die: str, ability_modifier: int, level: int = 1):
        hit_die_size = int(hit_die[1:])  # Extracts the number from 'd8', 'd10', etc.
        if level > 1:
            hit_die_size = randint(1, hit_die_size)
        self.max_hp += hit_die_size + ability_modifier
        self.current_hp = self.max_hp

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
        
    def increase_ability_score(self, ability: str, amount: int):
        if hasattr(self, ability):
            setattr(self, ability, getattr(self, ability) + amount)
        else:
            raise ValueError(f"Invalid ability score: {ability}")


class Proficencies:
    def __init__(self, armor: list[str], weapons: list[str], tools: list[str]):
        self.armor = armor
        self.weapons = weapons
        self.tools = tools
        

class Equipment:
    def __init__(self, armor: list[dict[str, Union[int, int]]], weapons: list[dict[str, Union[int, int]]],
                 tools: list[dict[str, Union[str, int]]], potions: list[dict[str, Union[str, int]]],
                 currency: list[dict[str, int]], misc: list[str]):
        self.armor = armor
        self.weapons = weapons
        self.tools = tools
        self.potions = potions
        self.currency = currency
        self.misc = misc


class CharacterClass:
    def __init__(self, name: str, hit_die: str, primary_abilities: list[str], saving_throws: list[str],
                 proficiencies : dict[str, list[str]], skills: list[str],
                 starting_equipment: list[str], starting_ability_scores: dict[str, int]):
        self.name = name
        self.hit_die = hit_die
        self.primary_abilities = primary_abilities
        self.saving_throws = saving_throws
        self.proficiencies  = proficiencies 
        self.skills = skills
        self.starting_equipment = starting_equipment
        self.starting_ability_scores = starting_ability_scores
        
    @classmethod
    def load_class(cls, class_name: str):
        # Load class data from a file or database
        classes_path = Path('data/classes.json')
        with open(classes_path, 'r') as f:
            classes = json.load(f)
        class_data = next([c for c in classes if c['name'] == class_name], None)
        if class_data:
            return cls(**class_data)
        else:
            raise ValueError(f"Class '{class_name}' not found")


class Race:
    def __init__(self, name: str, desc: str,
                 ability_bonuses: dict[str, int], size: int,
                 speed: int, traits: list[str], languages: list[str]):
        self.name = name
        self.description = desc
        self.ability_bonuses = ability_bonuses
        self.size = size
        self.speed = speed
        self.traits = traits
        self.languages = languages
    
    @classmethod
    def load_race(cls, race_name: str):
        # Load race data from a file or database
        races_path = Path('data/races.json')
        with open(races_path, 'r') as f:
            races = json.load(f)
        race = next([race for race in races if race['name'] == race_name], None)
        if race:
            return cls(**race)
        else:
            raise ValueError(f"Race '{race_name}' not found")
        
class Background:
    def __init__(self, name: str, desc: str, feature: dict[str, str],
                 skill_proficiencies: list[str], tool_proficiencies: list[str],
                 starting_equipment: list[str]):
        self.name = name
        self.description = desc
        self.skill_proficiencies = skill_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.equipment = starting_equipment
        self.feature = feature
    
    @classmethod
    def load_background(cls, background_name: str):
        # Load background data from a file or database
        backgrounds_path = Path('data/backgrounds.json')
        with open(backgrounds_path, 'r') as f:
            backgrounds = json.load(f)
        background = next([bg for bg in backgrounds if bg['name'] == background_name], None)
        if background:
            return cls(**background)
        else:
            raise ValueError(f"Background '{background_name}' not found")