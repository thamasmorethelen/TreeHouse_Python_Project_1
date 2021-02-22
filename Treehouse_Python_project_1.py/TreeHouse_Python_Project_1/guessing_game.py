"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import math


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
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

# Kick off the program by calling the start_game function.
start_game()

