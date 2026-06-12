#IMPORTS
from logging import NullHandler
from tkinter import *
import pandas
from random import choice

#CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
SELECTED_WORD = None
to_learn = []

# IMPORTING DATA
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# FUNCTIONS
def next_word():
    global SELECTED_WORD, flip_timer
    window.after_cancel(flip_timer)
    SELECTED_WORD = choice(to_learn)
    flashcard.itemconfig(card_side, image=card_front_image)
    flashcard.itemconfig(word, text=SELECTED_WORD["French"], fill="black")
    flashcard.itemconfig(language_name, text="French", fill="black")
    flip_timer = window.after(3000, flashcard_back)

def flashcard_back():
    flashcard.itemconfig(card_side, image=card_back_image)
    global SELECTED_WORD
    flashcard.itemconfig(language_name, text="English", fill ="white")
    flashcard.itemconfig(word, text=SELECTED_WORD["English"], fill="white")

def is_known():
    to_learn.remove(SELECTED_WORD)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_word()

# UI
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("flashy")

#canvas
flashcard = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_side = flashcard.create_image(400, 263, image=card_front_image)

language_name = flashcard.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word = flashcard.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

flashcard.grid(row=0, column=0, columnspan=2)

#buttons
wrong_tick_image = PhotoImage(file="./images/wrong.png")
wrong_tick_button = Button(image=wrong_tick_image, highlightthickness=0, command=next_word)
wrong_tick_button.grid(row=1, column=0)

right_tick_image = PhotoImage(file="./images/right.png")
right_tick_button = Button(image=right_tick_image, highlightthickness=0, command=is_known)
right_tick_button.grid(row=1, column=1)

#start
flip_timer = window.after(3000, flashcard_back)
next_word()

window.mainloop()