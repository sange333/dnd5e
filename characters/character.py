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
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Class: {self.char_class}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Dexterity: {self.dexterity}")
        print(f"Constitution: {self.constitution}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Wisdom: {self.wisdom}")
        print(f"Charisma: {self.charisma}\n")

    def attack(self):
        attack_roll = random.randint(1, 20) + self.strength
        print(f"{self.name} attacks! Rolled a {attack_roll}")
        return attack_roll

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage, remaining health: {self.health}\n")
