from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
CHECKMARK = "✔"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20

reps = 0
checkmarks = ""

def start():

    # ----------Reset-----------#

    def reset_timer():
        global reps
        global checkmarks
        global timer
        window.after_cancel(timer)
        canvas.itemconfig(timer_txt, text="00:00")
        checkmarks=""
        lbl_check.config(text=checkmarks)
        lbl_timer.config(text="TIMER")
        reps = 0

    # ----------Timer-----------#

    def start_timer():
        global checkmarks
        global reps
        print(reps)
        reps += 1
        if reps >= 8:
            count_down(LONG_BREAK_MIN * 60)
            lbl_timer.config(text="LONG BREAK", fg=RED)
            reps = 0
        elif reps % 2 == 0:
            count_down(SHORT_BREAK_MIN * 60)
            lbl_timer.config(text="BREAK", fg=PINK)
        else:
            count_down(WORK_MIN * 60)
            lbl_timer.config(text="WORK", fg=GREEN)
            checkmarks += CHECKMARK
            lbl_check.config(text=checkmarks)


    # ----------Countdown-----------#

    def count_down(count):

        count_min = int(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        act_time = f"{count_min}:{count_sec}"
        canvas.itemconfig(timer_txt, text=act_time)
        if count > 0:
            global timer
            timer = window.after(10, count_down, count - 1)
        elif count <= 0:
            start_timer()


    #----------UI-----------#
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=30, pady=30, bg=YELLOW)

    lbl_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW, highlightthickness=0)
    lbl_timer.grid(column=1, row=0)

    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=1, row=1)

    btn_start = Button(text="START", padx=20, pady=10, highlightthickness=0, command=start_timer)
    btn_start.grid(column=0, row=2)
    btn_reset = Button(text="RESET", padx=20, pady=10, highlightthickness=0, command=reset_timer)
    btn_reset.grid(column=2, row=2)

    lbl_check = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0, font=("Arial", 20))
    lbl_check.grid(column=1, row=3)

    window.mainloop()