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
    window.config(padx=30, pady=30, bg=YELLOW)

    lbl_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0)
    lbl_timer.grid(column=1, row=0)

    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=1, row=1)

    btn_start = Button(text="START")
    btn_start.grid(column=0, row=2)
    btn_reset = Button(text="RESET")
    btn_reset.grid(column=2, row=2)

    lbl_check = Label(text="✔", fg=GREEN, bg=YELLOW, highlightthickness=0, font=("Arial", 20))
    lbl_check.grid(column=1, row=3)

    window.mainloop()