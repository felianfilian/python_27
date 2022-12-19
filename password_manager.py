from tkinter import *

def start():
    window = Tk()
    window.title("Password Manager")
    canvas = Canvas(height=200, width=200)
    logo_img = PhotoImage(file="./pw_manager/logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.pack()

    window.mainloop()

