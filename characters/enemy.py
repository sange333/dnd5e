import random

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        attack_roll = random.randint(1, 20) + self.strength
        print(f"{self.name} 攻击! 掷出了 {attack_roll}")
        return attack_roll

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} 受到 {damage} 点伤害，剩余生命值: {self.health}\n")
