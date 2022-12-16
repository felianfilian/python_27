import tkinter
window = tkinter.Tk()
window.title("First GUI Project")
window.minsize(width=800, height=600)

my_label = tkinter.Label(text="MyLabel", font=("Arial", 24, "bold"))
my_label.pack(side="left")


window.mainloop()

