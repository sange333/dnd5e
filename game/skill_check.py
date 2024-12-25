import random

def skill_check(character, skill):
    print(f"{character.name} 正在进行 {skill} 检定...")
    roll = random.randint(1, 20) + getattr(character, skill)
    print(f"掷出了 {roll}")
    return roll
