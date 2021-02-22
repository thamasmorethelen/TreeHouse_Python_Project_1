"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
import math


def start_game():
    
    solution = random.randint(1,10)


    attempts = 2

    welcome = ("Hi! Welcome to the Number Guessing Game!!!")

    welcome_boarder = "-" * len(welcome)

    welcome_message = welcome_boarder + "\n" + welcome + "\n" + welcome_boarder 

    print(welcome_message)


    close =("Thanks for playing!!!")

    close_boarder = "-" * len(close)

    closing_message = close_boarder + "\n" + close + "\n" + close_boarder
    try:
        guess = int(input("Pick a number between 1 and 10: "))
    except ValueError:
        print("Oh No! That's not a valid value! Try again.")
    else:
        if guess == solution:
            print("Awesome Sause! You got it in {} attempt!".format(attempts))
            print(closing_message)
        while guess != solution:
            try:
                if guess < solution:
                    print("It's higher")
                    guess = int(input("Try again: "))
            except ValueError:
                print("Invalid Value, please try again")
            try:
                if guess > solution:
                    print("It's lower")
                    guess = int(input("Try again: "))
            except ValueError:
                print("Invalid Value, please try again")
            attempts += 1
            if guess == solution:
                print("Great job! You got it in {} attempts!".format(attempts))
                print(closing_message)


start_game()

