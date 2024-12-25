import time

def intro_scene():
    print("Welcome to the DnD5e Text Adventure Game!\n")
    time.sleep(1)
    print("You wake up in a dark forest with no memory of how you got here.")
    print("A path leads to the north, and you hear something moving in the bushes nearby.")
    print("What do you want to do?")
    print("1. Explore the bushes")
    print("2. Walk down the path to the north")
    print("3. Wait and listen\n")
    choice = input("Enter the number of your choice: ")
    
    return choice
