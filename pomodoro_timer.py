from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


def start():
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=30, pady=30)

    canvas = Canvas(width=200, height=224)
    tomato_ing = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_ing)
    canvas.pack()

    window.mainloop()