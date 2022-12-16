from tkinter import *

def start():
    window = Tk()
    window.title("First GUI Project")
    window.minsize(width=800, height=600)

    my_label = Label(text="MyLabel", font=("Arial", 24, "bold"))
    my_label.pack(side="left")

    def button_click():
        print("YES")

    # Button
    button = Button(text="Click", command=button_click)
    button.pack()

    window.mainloop()

