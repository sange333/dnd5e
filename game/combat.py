import random

def combat(character, enemy):
    print("\n一只野怪出现了!\n")
    while character.health > 0 and enemy.health > 0:
        print(f"\n{character.name} 的回合!")
        action = input("你想做什么?\n1. 攻击\n2. 防御\n3. 逃跑\n请输入你的选择: ")
        
        if action == "1":
            attack_roll = character.attack()
            if attack_roll >= 15:  # 示例命中条件
                damage = random.randint(3, 6)
                enemy.take_damage(damage)
            else:
                print(f"{character.name} 的攻击没有命中!\n")
        
        elif action == "2":
            print(f"{character.name} 进行防御。\n")
        
        elif action == "3":
            print(f"{character.name} 选择逃跑!\n")
            break
        
        if enemy.health > 0:
            print(f"{enemy.name} 的回合!")
            enemy_attack = enemy.attack()
            if enemy_attack >= 15:  # 示例命中条件
                damage = random.randint(2, 5)
                character.take_damage(damage)
            else:
                print(f"{enemy.name} 的攻击没有命中!\n")
