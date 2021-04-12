from random import choice
from tkinter import *

import pandas

BACKGROUND_COLOUR = "#424242"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_word = {}
flip_time = 3000


def next_card():
    global current_word, flip_time
    win.after_cancel(flip_time)
    current_word = choice(to_learn)
    canvas.itemconfig(card_bg, image=flash_card_f)
    canvas.itemconfig(card_word, text=current_word['French'])
    flip_time = win.after(3000, func=change_card)


def correct():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def change_card():
    canvas.itemconfig(card_bg, image=flash_card_e)
    canvas.itemconfig(card_word, text=current_word['English'])


# build GUI
win = Tk()
win.title("Flashy")
win.config(
    padx=50,
    pady=50,
    bg=BACKGROUND_COLOUR
)

flip_time = win.after(3000, func=change_card)

# image
flash_card_f = PhotoImage(file="images/french.png")
flash_card_e = PhotoImage(file="images/english.png")
key_tick = PhotoImage(file="images/key_1.png")
key_cross = PhotoImage(file="images/key_2.png")

canvas = Canvas(
    width=800,
    height=536,
    bg=BACKGROUND_COLOUR,
    highlightthickness=0
)

card_bg = canvas.create_image(
    400, 268,
    image=flash_card_f,
)

canvas.grid(column=1, row=0, columnspan=2)

# text
card_word = canvas.create_text(
    400, 263,
    text='',
    font=("Arial", 80, "bold")
)

# buttons
button_tick = Button(
    image=key_tick,
    highlightthickness=0,
    bg=BACKGROUND_COLOUR,
    command=correct
)

button_tick.grid(column=1, row=1)

button_cross = Button(
    image=key_cross,
    highlightthickness=0,
    bg=BACKGROUND_COLOUR,
    command=next_card
)

button_cross.grid(column=2, row=1)

next_card()

win.mainloop()
