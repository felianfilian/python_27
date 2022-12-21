from tkinter import *
from tkinter import messagebox
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def start():

    #-------Password Manager---------#
    def generate_pass():
        ent_pass.delete(0,END)

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = []

        pass_letters = [random.choice(letters) for _ in range(nr_letters)]
        pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
        pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

        password_list = pass_letters + pass_symbols + pass_numbers
        random.shuffle(password_list)

        password = "".join(password_list)
        ent_pass.insert(0,password)

    #-----------------#

    def save():
        my_website = ent_website.get()
        my_email = ent_mail.get()
        my_pass = ent_pass.get()

        if my_website=="" or my_email=="" or my_pass=="":
            messagebox.showinfo(title="Fields missing", message="Please fill out all the fields")
            return

        is_ok = messagebox.askokcancel(title=f"{my_website}", message="You want to save?")
        if is_ok:
            with open("./pw_manager/data.txt", mode="a") as file:
                save_data = f"{my_website} | {my_email} | {my_pass}\n"
                file.write(save_data)
                ent_website.delete(0, END)
                ent_mail.delete(0, END)
                ent_pass.delete(0, END)

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
    ent_mail.focus()
    ent_pass = Entry()
    ent_pass.grid(row=3, column=1, sticky="EW")

    btn_gen_pass = Button(text="Generate Password", command=generate_pass)
    btn_gen_pass.grid(row=3, column=2)
    btn_add = Button(text="Add", command=save)
    btn_add.grid(row=4, column=1, columnspan=2, sticky="EW")

    window.mainloop()

