import sys
import os
import textwrap

dirty_words = ("penis", "vagina", "pussy", "cock", "bastard", "fuck", "cunt", "dick")
inventory = ["Lint", "About £3.50 in loose change", "A floppy disk containing Leisure Suit Larry pt. 4"]


def open_inventory():
    print("\nYou currently have in your bag:")
    for i in inventory:
        print(f"] {i}")
    print()


def clear_console():
    # Clear the screen
    command = 'clear'
    if os.name in ('nt', 'dos'):
        # If player uses Windows (yuck), use cls instead
        command = 'cls'
    os.system(command)


def play_again():
    print("\nDo you want to play again? (y or n)")

    # Convert the players input to lower case
    answer = input(">").lower()

    if "y" in answer:
        # Start the game again
        start()
    else:
        # If the player types "n" or anything else
        clear_console()
        sys.exit()


def game_over(reason):
    # Print the reason supplied
    print(reason)
    print("\nGame Over!")
    play_again()


def diamond_room():
    # Give some prompts
    print(textwrap.fill("\nYou enter the room and even without any visible source of light, you see diamonds "
                        "glittering all across the room. Your eyes bulge at the sight (and a certain other area bulges "
                        "as well) and your mouth starts to salivate. All your hopes and dreams have come true, you can "
                        "finally pay off that student loan you've had for years. To the back of the room there is also "
                        "a door, which you hope leads to a early escape.",
                        width=70, replace_whitespace=False))
    print("\nWhat do you do? (1 or 2)")
    print(textwrap.fill("\n1) Take as many diamonds as you can physically hold and then run to the door",
                        width=70, replace_whitespace=False))
    print(textwrap.fill("2) Fear that there's some sort of trap and resist temptation, head towards the door with "
                        "empty pockets", width=70, replace_whitespace=False))

    while True:
        # Take player input
        answer = input("> ")

        if answer == "1":
            # Your greed kills you
            game_over(textwrap.fill("\nYour greed has brought upon you an early demise. Turns out the diamonds where "
                                    "cursed, like super cursed. The second you touched them, a great flash surged "
                                    "through your body. Your hands dissolve front of you. Your arms slowly melt away "
                                    "and it continues up your body, pain like you've never imagined before, until you "
                                    "see your vision melting away as well. Ouch, guess you still managed avoid paying "
                                    "that student loan at least.", width=70, replace_whitespace=False))
        elif answer == "2":
            print(textwrap.fill("\nYou walk towards the door, anguish filling your stomach from passing up this chance "
                                "of a life time. You tell yourself that you've just saved your own life and that some "
                                "dreary demise would have afflicted you, had you taken any of the diamonds.",
                                width=70, replace_whitespace=False))
            # Give player a chance to play again
            play_again()
        elif answer == "0":
            open_inventory()
        else:
            game_over(textwrap.fill("\nHow did you even make it this far in the game without being able to enter the "
                                    "right command?", width=70, replace_whitespace=False))


def monster_room():
    # Give some prompts
    print(textwrap.fill("\nYou enter the room and immediately see a massive, hulking monster. You feel a gurgle in "
                        "your stomach and suddenly your undergarments feel heavier. There's an ominous smell in the "
                        "air; you aren't sure if that's now coming from you or the monster. You regain your composure "
                        "quickly enough to realise that the monster is sleeping. The longer you look you kinda realise "
                        "it's snoring like a puppy. You wish you'd realised this before defecating in your pantaloons. "
                        "You also notice a door behind the monster.", width=70, replace_whitespace=False))
    print("\nWhat will you do? (1 or 2)")
    print(textwrap.fill("\n1) Try to sneakily walk around the monster and enter the door",
                        width=70, replace_whitespace=False))
    print(textwrap.fill("2) Avenge your soiled boxers and kill the monster while it sleeps, showing how \"courageous\" "
                        "you are", width=70, replace_whitespace=False))

    while True:
        # Take player input
        answer = input("> ")

        if answer == "1":
            # Move on to the Diamond Room
            diamond_room()
        elif answer == "2":
            # It's game over man, game over
            game_over(textwrap.fill("\nYour \"courage\" is worthless, just like you. The monster wakes up and with a "
                                    "shriek that could open the gates of Hell, devours you with ease. Kinda like a dog "
                                    "eating a Chicken Nugget.", width=70, replace_whitespace=False))
        elif answer == "0":
            open_inventory()
        else:
            game_over(textwrap.fill("\nIt's amazing to think you got this far in life without following simple "
                                    "commands.", width=70, replace_whitespace=False))


def bear_room():
    # Give some prompts
    print(textwrap.fill("\nYou enter the room and hear breathing. It doesn't take you long to suddenly realise that "
                        "you're in danger. Suddenly you hear a low, rumbling, growl. Your eyes quickly make contact "
                        "with what appears to be a bear in the corner. Thankfully at the moment it seems more "
                        "interested in what it's currently eating to be an immediate threat to you.",
                        width=70, replace_whitespace=False))
    print("\nWhat would you like to do? (1 or 2)")
    print("\n1) Try to take what the bear is eating")
    print("2) Taunt the bear")

    while True:
        # Take player input
        answer = input("> ")

        if answer == "1":
            # Welp, the player is dead
            game_over(textwrap.fill("\nWell that wasn't a smart idea! You don't go taking food away from a bear, that "
                                    "normally ends up with you becoming the food.", width=70, replace_whitespace=False))
        elif answer == "2":
            print(textwrap.fill("\nLuckily for you the bear doesn't want to fight, it takes it's food and moves "
                                "further away, revealing a door behind it. You, cautiously, move to and open the door.",
                                width=70, replace_whitespace=False))
            diamond_room()
        elif answer == "0":
            open_inventory()
        else:
            # Game Over time again!
            game_over(textwrap.fill("\nYou didn't enter a correct input. By this time the bear has finished it's food."
                                    "Seems the bear is still hungry though. Guess what's next for dinner? Or maybe,"
                                    "\"who's\" next for dinner.", width=70, replace_whitespace=False))


def start():
    # Clear the screen
    clear_console()

    # Start the game by prompting the player to take a path
    print("You are standing in a dark room.")
    print(textwrap.fill("\nFrom what you can make out, as your eyes start to adjust to the darkness, there is a room "
                        "to the left and a room to the right. Which do you choose?",
                        width=70, replace_whitespace=False))
    print("\n1) Left")
    print("2) Right")

    while True:
        # Take an input and make it lowercase
        answer = input("> ")

        if answer == "1":
            # Do this is the player picked "Left"
            bear_room()
        elif answer == "2":
            # Do this if the player picked "Right"
            monster_room()
        elif answer == "0":
            open_inventory()
        elif answer in dirty_words:
            game_over(textwrap.fill("\nHow dare you speak to me like that! A bolt of lightning strikes you from out of "
                                    "nowhere", width=70, replace_whitespace=False))
        else:
            # Call "game_over()" if the player doesn't enter a matching answer
            game_over("\nDo you really deserve to live if you can't answer a simple question?")


# Start the game
start()