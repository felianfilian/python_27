from tkinter import *

def start():
    window = Tk()
    window.title("Miles to Kilometers")
    # window.minsize(width=300, height=300)
    window.config(padx=50, pady=50)

    def calc_km():
        result = float(entry.get()) * 1.61
        label03.config(text=str(result))

    entry = Entry(width=10)
    entry.grid(column=1, row=0)

    label01 = Label(text="Miles")
    label01.grid(column=2, row=0)

    label02 = Label(text="is equal to")
    label02.grid(column=0, row=1)

    label03 = Label(text="0")
    label03.grid(column=1, row=1)

    label04 = Label(text="Km")
    label04.grid(column=2, row=1)

    btn_calc = Button(text="Calculate", command=calc_km)
    btn_calc.grid(column=1, row=2)

    window.mainloop()