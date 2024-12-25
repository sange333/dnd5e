import random

def skill_check(character, skill):
    print(f"{character.name} is attempting a {skill} check...")
    roll = random.randint(1, 20) + getattr(character, skill)
    print(f"Rolled a {roll}")
    return roll
