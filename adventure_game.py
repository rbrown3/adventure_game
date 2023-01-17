import time

import random
characters = ["Jazmin", "Tobi", "Lana", "Carmen", "Brad", "Jeremy", "Shelby",
              "Anthony", "Ben", "Kathy", "Jen", "Jun"]

keys = ["small", "medium", "large"]


def pause_print(message_to_print, pause_length):
    print(message_to_print)
    time.sleep(pause_length)


def intro():
    pause_print("You wake up from what you thought was a dream."
                "However, you quickly realize that you are"
                "in a different world."
                "Everything is grey even the people.", 2)
    pause_print("All of their hearts are blue, literally!", 2)
    pause_print("Your goal is to help each heart turn red.", 2)
    pause_print("Hearts only turn red when they find joy and happiness.", 2)


def random_character(characters):
    copy_characters = characters[:]
    character = copy_characters.pop(random.randrange(len(copy_characters)))
    return character


def meet_character(character):
    pause_print("Someone approaches you and shyly introduces themselves.", 2)
    pause_print("Hi, my name is " + character + "."
                "I heard you have the key to happiness.", 2)


def win_lose(character):
    messages = ["This heart is red and beaming with joy!",
                "This heart is hopeless",
                "This heart is so grateful and full of joy!",
                "This heart will never be red.",
                "This heart never thought joy would be possible!",
                "This heart is growing even more gloomy.",
                "This heart is still blue.",
                "This heart is overflowing with joy!",
                "This heart is rejoicing with joy.",
                "There is joy in this heart!",
                "This heart is so blue!",
                "This heart is as blue as the ocean."]
    message = random.choice(messages)
    if "joy" in message:
        if "red" in message:
            pause_print(message, 2)
            pause_print("You won the game!", 2)
        else:
            pause_print(message, 2)
            pause_print("You almost made this heart red! Don't give up!", 2)
    else:
        pause_print(message, 2)
        pause_print("Try again!", 2)


def play_again():
    response = input("Would you like to play again?"
                     "yes or no").lower()
    if "yes" in response:
        play_game()
    elif "no" in response:
        pause_print("Goodbye for now!", 2)
    else:
        pause_print("Sorry, I don't understand.", 2)
        play_again()


def choose_key(keys):
    while True:
        key = input("You reach into your bag and take out a key."
                    "What  size is the key? "
                    "small "
                    "medium "
                    "large ").lower()
        if key == "small":
            return key
        elif key == "medium":
            return key
        elif key == "large":
            return key
        else:
            pause_print("I don't understand.", 2)


def play_game():
    intro()
    character = random_character(characters)
    meet_character(character)
    key = choose_key(keys)
    win_lose(character)
    play_again()

if __name__ == "__main__":
    play_game()


# resources:
# choosing a random item from array without duplicates-
# https://stackoverflow.com/questions/
# 10048069/what-is-the-most-pythonic-way-to-pop-a-random-element-from-a-list

# how to use the output for one function as a parameter for another-
# https://stackoverflow.com/questions/54736309/
# how-to-use-output-for-one-function-as-parameter-for-another
