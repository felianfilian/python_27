from tkinter import *

def start():
    window = Tk()
    window.title("Password Manager")
    window.config(padx=40, pady=40)

    canvas = Canvas(height=200, width=200)
    logo_img = PhotoImage(file="./pw_manager/logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

    lbl_website = Label(text="Website", padx=20)
    lbl_website.grid(row=1, column=0)
    lbl_mail = Label(text="Email", padx=20)
    lbl_mail.grid(row=2, column=0)
    lbl_pass = Label(text="Password", padx=20)
    lbl_pass.grid(row=3, column=0)

    ent_website = Entry()
    ent_website.grid(row=1, column=1, columnspan=2, sticky="EW")
    ent_mail = Entry()
    ent_mail.grid(row=2, column=1, columnspan=2, sticky="EW")
    ent_mail.insert(0, "peter@reter.pot")
    ent_pass = Entry()
    ent_pass.grid(row=3, column=1, sticky="EW")

    btn_gen_pass = Button(text="Generate Password", padx=20)
    btn_gen_pass.grid(row=3, column=2)
    btn_add = Button(text="Add")
    btn_add.grid(row=4, column=1, columnspan=2, sticky="EW")

    window.mainloop()

