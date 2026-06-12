from random import randint
from art import logo

def random_num():
    return randint(1,100)

def difficulty(mode):
    if mode == "easy":
        return 10
    else:
        return 5

def game():
    print(logo)
    print("I am guessing a number between 1 and 100. Try guessing it")
    level = input("Choose a difficulty [ easy / hard ]: ").lower()
    lives = difficulty(level)

    num = random_num()

    while lives != 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == num:
            print(f"You got it! The answer was {guess}.")
            return True

        elif guess < num:
            print("Too low")
            lives -= 1

        else:
            print("Too high")
            lives -= 1
    print("You've run out of guesses. Refresh the page to run again.")
    return True


game_over = False
while not game_over:
    game_over = game()