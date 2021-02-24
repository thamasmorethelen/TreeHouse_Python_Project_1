
"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random
import math
def messaging(message):
    boarder = "-" * len(message)
    complete_message = boarder + "\n" + message + "\n" + boarder
    print(complete_message)

def start_game():
   
    solution = random.randint(1,10)

    attempts = 0

    welcome = "Hi! Welcome to the Number Guessing Game!!!"

    close ="Thanks for playing!!!"

    messaging(welcome)
    
    guess = int("0")
    
    while guess != solution:
        attempts += 1
        try:
            guess = int(input("Pick a number between 1 and 10: "))
            
            if guess == solution:
                print("Awesome Sause! You got it in {} attempt!".format(attempts))
                messaging(close)
            
        except ValueError:
            print("Oh No! That's not a valid value!")
            
        else:
            while guess != solution:
                attempts += 1    
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
                
                    
                if guess == solution:
                    print("Awesome Sause! You got it in {} attempt!".format(attempts))
                    messaging(close)
                    

start_game()

