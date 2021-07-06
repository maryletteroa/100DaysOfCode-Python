from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import choice

from pandas._config import config

BACKGROUND_COLOR = "#B1DDC6"

# ---- Parse words file ---- #

try:
    data = pd.read_csv("./data/words_to_learn.csv", header=0)
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv", header=0)
finally:
    to_learn = data.to_dict(orient="records")
    current_card = {}

# ---- Get words ---- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = choice(to_learn)
    except IndexError:
        messagebox.showinfo(title="Oops", message="No more words to learn")
    canvas.itemconfig(image_canvas, image = front_img)
    canvas.itemconfig(language_canvas, text="French", fill="black")
    canvas.itemconfig(word_canvas, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(image_canvas, image = back_img)
    canvas.itemconfig(language_canvas, text="English", fill="white")
    canvas.itemconfig(word_canvas, text=current_card["English"], fill="white")

def know():
    next_card()
    if current_card in to_learn:
        to_learn.remove(current_card)
    else:
        messagebox.showinfo(title="Oops", message="No more words to learn")

    # ---- To learn CSV---- #
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
# ---- UI ---- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(3000, func=flip_card)


# Images
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image_canvas = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

language_canvas = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# Buttons
right_button = Button(image=right_img, highlightthickness=0, command=know)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()

