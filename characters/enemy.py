import random

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        attack_roll = random.randint(1, 20) + self.strength
        print(f"{self.name} attacks! Rolled a {attack_roll}")
        return attack_roll

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage, remaining health: {self.health}\n")
