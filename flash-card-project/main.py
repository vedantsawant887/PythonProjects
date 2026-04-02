from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("FLASH CARD APP")
window.config(background=BACKGROUND_COLOR,padx=50,pady=50)

current_word = {}
words = {}

try:
    dataframe = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = dataframe.to_dict(orient="records")




def change_word():
    global current_word,flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words)
    french_word = current_word["French"]
    canvas.itemconfig(language, text="French",fill="black")
    canvas.itemconfig(word, text=french_word,fill="black")
    canvas.itemconfig(card, image=card_front_image)
    flip_timer = window.after(ms=3000, func=change_card)

def change_card():
    canvas.itemconfig(card,image=card_back_image)
    canvas.itemconfig(language, text="English",fill="white")
    english_mean = current_word["English"]
    canvas.itemconfig(word, text=english_mean,fill="white")

def update():
    words.remove(current_word)
    data = pandas.DataFrame(words)
    data.to_csv("./data/words_to_learn.csv",index=False)
    change_word()


flip_timer = window.after(ms=3000, func=change_card)








canvas = Canvas()
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 270, image=card_front_image)
language = canvas.create_text(399,150,text="Language",fill="black",font=("ariel",40,"italic"),)
word = canvas.create_text(399,263,text="Word",fill="black",font=("ariel",60,"bold"),)
canvas.config(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

right_button = Button()
right_image = PhotoImage(file="./images/right.png")
right_button.config(image=right_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=update)
right_button.grid(row=1,column=0)

wrong_button = Button()
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button.config(image=wrong_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=change_word)
wrong_button.grid(row=1,column=1)

change_word()










window.mainloop()