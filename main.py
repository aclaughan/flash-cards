from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOUR = "#424242"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")





def next_card():
    word = choice(to_learn)['French']
    canvas.itemconfig(card_word, text=word)

# build GUI

win = Tk()
win.title("Flashy")
win.config(
    padx=50,
    pady=50,
    bg=BACKGROUND_COLOUR
)

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

canvas.create_image(
    400, 268,
    image=flash_card_f,
)

canvas.grid(column=1, row=0, columnspan=2)

# text
card_word = canvas.create_text(
    400,263,
    text="word",
    font=("Arial", 80, "bold")
)


# buttons
button_tick = Button(
    image = key_tick,
    highlightthickness=0,
    bg=BACKGROUND_COLOUR,
    command=next_card
)

button_tick.grid(column=1,row=1)

button_cross = Button(
    image = key_cross,
    highlightthickness=0,
    bg=BACKGROUND_COLOUR,
    command=next_card
)

button_cross.grid(column=2,row=1)

next_card()

win.mainloop()
