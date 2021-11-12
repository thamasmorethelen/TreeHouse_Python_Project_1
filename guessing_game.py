import random
import sys


def display_message(message):
    boarder = "=" * len(message)
    print(f"\n\n{boarder} \n{message} \n{boarder}\n")


display_message('Welcome to the Number Guessing Game!')


def start_game():
    random_num = random.choice(range(1, 11))
    attempts = 1
    highscore = []
    guess = ' '
    play_again = True
    print('A random number has been generated your goal is to guess it!')
    print(random_num)
    while play_again:
        try:
            guess = input('Go ahead and guess: ')
            guess = int(guess)
            if guess not in range(1, 11):
                attempts += 1
                print("Hey man that's not in the range. Try again.") 
            elif guess == random_num:
                highscore.append(attempts)
                print(f"You Win! It took you {attempts} nice job!")
                attempts += 1
                play_again = input("Do you want to play again (Y)es/(N)o: ").upper()
                if play_again == "YES" or play_again == 'Y':
                    attempts = 0
                    print(f"\nThe current high score is {min(highscore)}")
                    start_game()
                if play_again == "NO" or play_again == "N":
                    print("No? Ok have a nice day!")
                    play_again = False
                    sys.exit()
            elif guess > random_num:
                attempts += 1
                print('Too high! Try again!')
            elif guess < random_num:
                attempts += 1
                print('Too low! Try again!')
            else:
                attempts += 1
                print('You lose!')
        except ValueError:
            attempts += 1
            print("Easy tiger numbers only please!")


start_game()