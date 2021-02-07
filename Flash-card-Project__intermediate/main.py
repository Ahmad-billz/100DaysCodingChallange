from random import choice
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Ariel", 24, "italic")
FONT_WORD = ("Ariel", 34, "bold")
flip_timer = 0
current_card = {}


try:
    data = pandas.read_csv("Data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# this one also works and makes a similar dictionary
# to_learn = {}
# for item in range(len(data_dict['Deutsch'])):
#     dict_improved[data_dict['Deutsch'][item]] = data_dict['English'][item]
# print(to_learn)


def show_card():
    global current_card
    current_card = choice(to_learn)
    canvas.itemconfig(canvas_photo, image=c_front)
    canvas.itemconfig(card_title, text=f"Deutsch", fill='black')
    canvas.itemconfig(card_word, text=f"{current_card['Deutsch']}", fill='black')
    global flip_timer
    flip_timer = window.after(3000, switch)


def switch():
    canvas.itemconfig(canvas_photo, image=c_back)
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill='white')


def right():
    global flip_timer
    window.after_cancel(flip_timer)
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    show_card()


def wrong():
    global flip_timer
    window.after_cancel(flip_timer)
    show_card()


window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
c_front = PhotoImage(file="images/card_front.png")
c_back = PhotoImage(file="images/card_back.png")
canvas_photo = canvas.create_image(400, 264, image=c_front)
card_title = canvas.create_text(400, 150, text="", font=FONT_TITLE)
card_word = canvas.create_text(400, 265, text="", font=FONT_WORD)
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=wrong)
wrong_btn.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, borderwidth=0, command=right)
right_btn.grid(column=1, row=1)

show_card()

window.mainloop()
