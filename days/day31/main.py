from tkinter import *

import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Courier", 35, "italic")
FONT1 = ("Courier", 55, "bold")
current_word = {}
to_learn= {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records") #Change the data to dictionary  by 2 rows like key:value


def next_card():
    """Returns a random French word from the dataset."""
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)  # Pick a random dictionary
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=old_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=current_word["English"])
    canvas.itemconfig(canvas_image, image=new_img)


def is_known():
    to_learn.remove(current_word)
    print(len(to_learn))
    pandas.DataFrame(to_learn)
    data.to_csv("data/words_to learn", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #


# Create a window
window = Tk()
window.title("Flashly")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_card)

# Load the image
not_approved_img = PhotoImage(file="images/wrong.png")
approved_img = PhotoImage(file="images/right.png")
old_img = PhotoImage(file="images/card_front.png")
new_img = PhotoImage(file="images/card_back.png")


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 270, image=old_img)
title_text = canvas.create_text(400, 150, text="", font=FONT)
word_text = canvas.create_text(400, 250, text="", font=FONT1)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
button_approved = Button(image=approved_img, highlightthickness=0, command=is_known)
button_approved.grid(row=2, column=1)
button_not_approved = Button(image=not_approved_img, highlightthickness=0, command=next_card)
button_not_approved.grid(row=2, column=0)


next_card()
window.mainloop()
