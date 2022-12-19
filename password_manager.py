from tkinter import *

def start():
    window = Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)
    canvas = Canvas(height=200, width=200)
    logo_img = PhotoImage(file="./pw_manager/logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(column=1, row=0)

    lbl_website = Label(text="Website")
    lbl_website.grid(column=0, row=1)
    ent_website = Entry(width=40)
    ent_website.grid(column=1, row=1, columnspan=2)

    lbl_mail = Label(text="Email")
    lbl_mail.grid(column=0, row=2)
    ent_mail = Entry(width=40)
    ent_mail.grid(column=1, row=2, columnspan=2)

    lbl_pass = Label(text="Password")
    lbl_pass.grid(column=0, row=3)
    ent_pass = Entry(width=21)
    ent_pass.grid(column=1, row=3)
    btn_gen_pass = Button(text="Generate Password")
    btn_gen_pass.grid(column=2, row=3)

    btn_add = Button(text="Add", width=36)
    btn_add.grid(column=1, row=4, columnspan=2)

    window.mainloop()

