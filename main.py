from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn ={}
# ____________________________button____________________________________

# data=DataFrame.to_dict(orient="records")
try:
    data =pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data =pd.read_csv("data/french_words.csv")
    to_learn =original_data.to_dict(orient="records")
else:
    to_learn= data.to_dict(orient="records") #it will take colum wise data make a separate dict

def next_card():
   global current_card,flip_timer
   window.after_cancel(flip_timer)
   current_card= random.choice(to_learn)
   canvas.itemconfig(title,text="French",fill="black")
   canvas.itemconfig(word,text= current_card["French"],fill="black")
   canvas.itemconfig(bg_image, image=card_front_img)
   window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(word, text=current_card["English"],fill="white")
    canvas.itemconfig(bg_image, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data =pd.DataFrame(to_learn)
    data.to_csv("data/to_learn.csv",index =False)
    next_card()

# ____________________________UI____________________________________

window=Tk()
window.title("Flashy")
window.config(padx= 50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card)

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

bg_image = canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
word =canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"))


cross_image=PhotoImage(file="images/wrong.png")
cross_button = Button(image = cross_image ,highlightthickness=0,command =next_card)
cross_button.grid(column=0, row=1 )

check_image=PhotoImage(file="images/right.png")
check_button = Button(image = check_image,highlightthickness=0 ,command =is_known)
check_button.grid(column=1, row=1 )


next_card()




window.mainloop()