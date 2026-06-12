import random
from art import logo, vs
from game_data import data


def option():
    return random.choice(data)


def winner(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == 'A'
    else:
        return guess == 'B'


print(logo)
score = 0
game_over = False

b = option()

while not game_over:
    a = b
    b = option()

    while a == b:
        b = option()

    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    followers_a = a['follower_count']
    followers_b = b['follower_count']

    print("\n" * 20)
    print(logo)

    if winner(guess, followers_a, followers_b):
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong answer. Final score: {score}")
        game_over = True