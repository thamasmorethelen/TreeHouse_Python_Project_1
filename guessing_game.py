import random

guess = " "
play_again = " "
welcome = ("Hi! Welcome to the Number Guessing Game!!!")
close = ("Thanks for playing!!!")


def welcome_closing(text):
    boarder = "-" * len(text)
    message = f" {boarder}\n {text}\n {boarder}"
    print(message)


def start_game():

    solution = random.randint(1, 10)
    attempts = 0
    welcome_closing(welcome)
    guess = ' '

    while guess != solution:

        try:
            attempts += 1
            if attempts == 2:
                guess = int(input("Pick a number between 1 and 10: "))
                attempts += 1
            if guess not in range(1, 11):
                print("Please enter a number in the given range, 1-10")
                guess = int(input("Try again: "))

            if guess < solution:
                print("It's higher")
                guess = int(input("Try again: "))

            if guess > solution:
                print("It's lower")
                guess = int(input("Try again: "))

            if guess == solution:
                print(f"Great job! You got it in {attempts} attempts!")
                welcome_closing(close)

        except ValueError:
            print("Invalid Value, please try again.")


start_game()
