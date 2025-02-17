

class CharacterClass:
    def __init__(self, name, hit_die, primary_ability, saving_throws, armor, weapons, tools, skills, equipment):
        self.name = name
        self.hit_die = hit_die
        self.primary_ability = primary_ability
        self.saving_throws = saving_throws
        self.armor = armor
        self.weapons = weapons
        self.tools = tools
        self.skills = skills
        self.equipment = equipment


class Race:
    def __init__(self, name, ability_bonuses, size, speed, darkvision, languages, traits):
        self.name = name
        self.ability_bonuses = ability_bonuses
        self.size = size
        self.speed = speed
        self.darkvision = darkvision
        self.languages = languages
        self.traits = traits
        
        
class Background:
    def __init__(self, name, skill_proficiencies, tool_proficiencies, languages, equipment, feature, trait):
        self.name = name
        self.skill_proficiencies = skill_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.languages = languages
        self.equipment = equipment
        self.feature = feature
        self.trait = trait