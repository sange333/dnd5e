import random

class Character:
    def __init__(self, name, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.health = 10
        self.strength = random.randint(8, 18)
        self.dexterity = random.randint(8, 18)
        self.constitution = random.randint(8, 18)
        self.intelligence = random.randint(8, 18)
        self.wisdom = random.randint(8, 18)
        self.charisma = random.randint(8, 18)
    
    def display_stats(self):
        print(f"名字: {self.name}")
        print(f"种族: {self.race}")
        print(f"职业: {self.char_class}")
        print(f"生命值: {self.health}")
        print(f"力量: {self.strength}")
        print(f"敏捷: {self.dexterity}")
        print(f"体质: {self.constitution}")
        print(f"智力: {self.intelligence}")
        print(f"智慧: {self.wisdom}")
        print(f"魅力: {self.charisma}\n")

    def attack(self):
        attack_roll = random.randint(1, 20) + self.strength
        print(f"{self.name} 攻击! 掷出了 {attack_roll}")
        return attack_roll

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} 受到 {damage} 点伤害，剩余生命值: {self.health}\n")
