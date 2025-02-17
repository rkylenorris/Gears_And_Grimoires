from random import choice
import math

def roll_ability_score():
    d6 = range(1, 7, 1)
    ability_nums = []
    
    for _ in range(4):
        ability_nums.append(choice(d6))
    
    min_roll = min(ability_nums)
    ability_nums.pop(ability_nums.index(min_roll))
    
    return sum(ability_nums)


def calculate_ability_modifier(ability_score: int) -> int:
    return math.floor((ability_score - 10) / 2)
    

def get_ability_scores():
    rolls = []
    for i in range(6):
        score = roll_ability_score()
        modifier = calculate_ability_modifier(score)
        roll = i + 1
        rolls.append({
            "ability_score": score,
            "ability_modifier": modifier
        })
    return rolls
        

def set_ability_scores() -> list:
    # roll for ability scores, return sorted desc by score
    ability_scores = sorted(get_ability_scores(), key=lambda d: d['ability_score'], reverse=True)
    
    # define abilities
    abilities = {
        'strength': 'measures physical power',
        'dexterity': 'measures agility',
        'constitution': 'measures endurance',
        'intelligence': 'measures reasoning and memory',
        'wisdom': 'measures perception and insight',
        'charisma': 'measures force of personality',
    }
    print("You can choose from the following abilities:")
    for k, v in abilities.items():
        print(f"\t{k}: {v}")
    
    # initialize empty array for choices
    chosen_scores = []

    # loop over scores and get player choices for each score
    for entry in ability_scores:
        score = entry['ability_score']
        modifier = entry['ability_modifier']
        msg = f"""Ability Score: {score}, modifier: {modifier} \n
                With which ability do you wish to associated this score? \n
                Choices remaining: {abilities.keys()}  
        """
        print(msg)
        choice = input().lower().strip()
        
        while choice not in abilities.keys():
            print(f"{choice.strip()} is not one of the abilities listed")
            print(f"Choices are {abilities.keys()}")
            choice = input('Type ability to associate with score {score}: ').lower().strip()
        
        if choice in abilities.keys():
            chosen_scores.append({
                "Ability": choice,
                "Score": score,
                "Modifier": modifier
            })
            del abilities[choice]
        
    return chosen_scores

            
        
        
set_scores = set_ability_scores()

print(set_scores)
