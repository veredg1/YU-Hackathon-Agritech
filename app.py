import tkinter
from tkinter import Tk
from tkinter import *

home: Tk = tkinter.Tk()
home.title("Home Page")
home.geometry('600x600')


b = Menubutton()
def showMessage():


    label = Label(text="Please enter your name ")
    label.pack()
    entry = Entry()
    entry.focus_set()
    entry.pack()
    entry.get()

    label = Label(text="suppliers enter 0, producers enter 1, consumers enter 2 ")
    label.pack()
    entry = Entry()
    entry.focus_set()
    entry.pack()
    entry.get()





button = tkinter.Button(home, text="create account", command = showMessage())


button.pack()


home.mainloop()
