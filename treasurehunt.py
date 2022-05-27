def treasure():
    print("\nYou are now in a treasure room!")
    print("And there is a door too!")
    print("What would you do? (1 or 2)")
    print("1). Take treasure and go through the door.")
    print("2). Just go through the door.")
    answer = input(">")
    if answer == "1":
        game_over("Treasure is not real,and i will make you die!")
    elif answer == "2":
        print("\n Congrats you win the game!")
        play_again()
    else:
        game_over("Enter a Number Dude!!")
def snake_room():
    print("\nThere are snakes here.")
    print("Behind the snake is another door.")
    print("Snakes are sleeping!")
    print("What would you do? (1 or 2)")
    print("1). Disturb them.")
    print("2).  You go without making noise.")
    answer = input(">")
    if answer == "1":
        game_over("Snakes will kill you.")
    elif answer == "2":
        print("\n Good choice,You can go out through door now!")
        treasure()
    else:
        game_over("Enter a Number Dude!!")
def monster_room():
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping.\nBehind the monster, there is another door. What would you do? (1 or 2)")
    print("1). Go through the door silently.")
    print("2).Be Brave, Kill the monster and show your courage!")
    answer = input(">")
    if answer == "1":
        treasure()
    elif answer == "2":
        game_over("The monster was hungry, he/it ate you.")
    else:
        game_over("Enter a Number Dude!!.")
def play_again():
    print("\nDo you want to play again? (y or n)")
    answer = input(">").lower()
    if "y" in answer:
        start()
    else:
        exit()
def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    play_again()
def start():
    print("\nYou are standing in a dark room.")
    print("There is a door to your left and right, which one do you take? (l or r)")
    answer = input(">").lower()
    if "l" in answer:
        snake_room()
    elif "r" in answer:
        monster_room()
    else:
        game_over("Enter a Number properly?")
start()
