from tkinter import *

def start():
    window = Tk()
    window.title("First GUI Project")
    window.minsize(width=800, height=600)

    def button_click():
        my_label.config(text=f"{input.get()}")

    my_label = Label(text="MyLabel", font=("Arial", 24, "bold"))
    my_label.grid(column=0, row=0)

    # Button
    button = Button(text="Click", command=button_click)
    button.grid(column=1, row=1)

    button2 = Button(text="Click", command=button_click)
    button2.grid(column=3, row=0)

    # Entry
    input = Entry(width=10)
    input.grid(column=4, row=3)



    window.mainloop()

