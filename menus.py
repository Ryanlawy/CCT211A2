import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb


def makemenu(win):
    top_menu = tk.Menu(win)  # win=top-level window
    menu = Menu(top_menu, name='name')
    menu.add_command(label="Crew and Credit", command=show_text)
    top_menu.add_cascade(label="Drama BookClub", menu=menu)



    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(top_menu, tearoff=0)
    filemenu.add_command(label="Logout", command=to_login)
    filemenu.add_command(label="User", command=to_user)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=win.quit)

    top_menu.add_cascade(label="View", menu=filemenu)

    # Navigate menus
    nevmenu = Menu(top_menu, tearoff=0)
    nevmenu.add_command(label="Back", command=Back)
    nevmenu.add_command(label="Search", command=to_login)
    nevmenu.add_command(label="Page Info", command=show_text)
    top_menu.add_cascade(label="Navigate", menu=nevmenu)

    helpmenu = Menu(top_menu, tearoff=0)
    helpmenu.add_command(label="About", command=show_text)
    top_menu.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    win.config(menu=top_menu)


def to_login():
    # take to login
    print("yeah")

def to_user():
    # take to user page
    print("Oh Yeah")

def show_text():
    # show a page of info
    print("")

def Back():
    # take to main page and login
    print("Stuff")
