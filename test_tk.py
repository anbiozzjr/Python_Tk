from tkinter import *

root = Tk()
choices = ["apple", "orange", "banana"]
choicesvar = StringVar(value=choices)

choices.append("nigga")
choicesvar.set(choices)

l = Listbox(listvariable=choicesvar)
l.pack()

root.mainloop()