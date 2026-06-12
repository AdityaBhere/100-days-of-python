import random
from hangman_words import word_list
import hangman_art

lives = 6

print(hangman_art.logo)
chosen_word = random.choice(word_list)

placeholder = "_" * len(chosen_word)
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = set()

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed: {guess}")
        continue

    guessed_letters.add(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # wrong guess handling
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print(f"*********************** YOU LOSE ***********************")
            print(f"The word was: {chosen_word}")

    # win condition
    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    print(hangman_art.stages[lives])
