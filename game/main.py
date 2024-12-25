from characters.character import Character
from characters.enemy import Enemy
from game.intro_scene import intro_scene
from game.combat import combat

def create_character():
    print("Let's create your character!")
    name = input("Enter your character's name: ")
    race = input("Enter your character's race (e.g., Human, Elf, Dwarf): ")
    char_class = input("Enter your character's class (e.g., Fighter, Wizard, Rogue): ")
    character = Character(name, race, char_class)
    print("\nCharacter created successfully!\n")
    character.display_stats()
    return character

def main():
    character = create_character()
    choice = intro_scene()
    
    if choice == "1":
        print("\nYou approach the bushes cautiously...")
        print("Suddenly, a wild wolf jumps out at you!")
        enemy = Enemy("Wolf", 20, 5)
        combat(character, enemy)
    
    elif choice == "2":
        print("\nYou start walking down the path to the north...")
        print("The path is clear, but you feel something lurking nearby...\n")
    
    elif choice == "3":
        print("\nYou decide to wait and listen...")
        print("You hear footsteps approaching...\n")
        enemy = Enemy("Goblin", 15, 4)
        combat(character, enemy)

if __name__ == "__main__":
    main()
