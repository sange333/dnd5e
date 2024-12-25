import random

def combat(character, enemy):
    print("\nA wild enemy appears!\n")
    while character.health > 0 and enemy.health > 0:
        print(f"\n{character.name}'s turn!")
        action = input("What do you want to do?\n1. Attack\n2. Defend\n3. Flee\nEnter your choice: ")
        
        if action == "1":
            attack_roll = character.attack()
            if attack_roll >= 15:  # Example hit condition
                damage = random.randint(3, 6)
                enemy.take_damage(damage)
            else:
                print(f"{character.name}'s attack missed!\n")
        
        elif action == "2":
            print(f"{character.name} defends.\n")
        
        elif action == "3":
            print(f"{character.name} flees!\n")
            break
        
        if enemy.health > 0:
            print(f"{enemy.name}'s turn!")
            enemy_attack = enemy.attack()
            if enemy_attack >= 15:  # Example hit condition
                damage = random.randint(2, 5)
                character.take_damage(damage)
            else:
                print(f"{enemy.name}'s attack missed!\n")
