import sys
import os

# 将项目根目录添加到 sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from characters.character import Character
from characters.enemy import Enemy
from game.intro_scene import intro_scene
from game.combat import combat


def create_character():
    print("让我们来创建你的角色吧!")
    name = input("请输入你的角色名字: ")
    race = input("请输入你的角色种族（例如：人类、精灵、矮人）: ")
    char_class = input("请输入你的角色职业（例如：战士、法师、盗贼）: ")
    character = Character(name, race, char_class)
    print("\n角色创建成功!\n")
    character.display_stats()
    return character

def main():
    character = create_character()
    choice = intro_scene()
    
    if choice == "1":
        print("\n你小心地走向灌木丛...")
        print("突然，一只野狼跳了出来!")
        enemy = Enemy("野狼", 20, 5)
        combat(character, enemy)
    
    elif choice == "2":
        print("\n你沿着小路往北走...")
        print("路面平坦，但你感觉周围有些不安的气息...\n")
    
    elif choice == "3":
        print("\n你决定停下来，静静地聆听...")
        print("你听到附近有脚步声...\n")
        enemy = Enemy("哥布林", 15, 4)
        combat(character, enemy)

if __name__ == "__main__":
    main()
