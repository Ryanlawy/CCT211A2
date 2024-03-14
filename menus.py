import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb


def makemenu(win):
    top_menu = tk.Menu(win)  # win=top-level window
    menu = Menu(top_menu, name='top')
    top_menu.add_cascade(label="Drama BookClub", menu=menu)
    menu.add_separator()

    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(top_menu, tearoff=0)
    filemenu.add_command(label="Logout", command=to_login)
    filemenu.add_command(label="User", command=to_user)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=win.quit)

    top_menu.add_cascade(label="Navigate", menu=filemenu)

    # create more pulldown menus
    nevmenu = Menu(top_menu, tearoff=0)
    nevmenu.add_command(label="Cut", command=)
    nevmenu.add_command(label="Copy", command=)
    nevmenu.add_command(label="Paste", command=)
    top_menu.add_cascade(label="Edit", menu=editmenu)

    helpmenu = Menu(top_menu, tearoff=0)
    helpmenu.add_command(label="About", command=)
    top_menu.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    win.config(menu=top_menu)


def to_login():
    # take to login
    print("yeah")

def to_user():
    # take to user page
    print("Oh Yeah")
