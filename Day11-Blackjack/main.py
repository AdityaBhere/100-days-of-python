import random
from art import logo


def deal_card():
    """Chooses a random card from the deck and returns it."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(hand):
    """Calculates the total score of the hand, tracking Blackjacks and Aces."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    while sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


def compare(user_score, computer_score):
    """Compares the user score against the computer score to determine the winner."""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def blackjack():
    print(logo)

    player_hand = []
    computer_hand = []
    game_over = False

    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            if input("Do you want another card (y/n): ").lower() == 'y':
                player_hand.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"\nYour final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Want to play a round of blackjack? (y/n): ").lower() == 'y':
    print("\n" * 20)
    blackjack()
