import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb
from login import Login
import main_page
from credit import Credit
import main



def makemenu(win):
    top_menu = tk.Menu(win)  # win=top-level window
    menu = Menu(top_menu, name='name')
    menu.add_command(label="Crew and Credit", command=show_text)
    top_menu.add_cascade(label="Drama BookClub", menu=menu)



    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(top_menu, tearoff=0)
    filemenu.add_command(label="Logout", command=lambda: to_login(win))
    filemenu.add_command(label="User", command=lambda: to_user(win))
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



def to_login(win):
    win.destroy()  # This destroys the current window
    # login_win = tk.Tk()  # Use Tk() for the main window of the application, Toplevel() for subsidiary windows
    # login_win.title("Login")
    # login_win.geometry("400x300")
    main.main()
    # Login(login_win)
    # login_win.  # Start the application

def to_user():
    login_win = tk.Toplevel()
    login_win.title("login")
    login_win.geometry("400x300")
    Login(login_win)

def show_text(win):
    win.destroy()
    credit_win = tk.Tk()
    credit_win.title("Credits")
    credit_win.geometry("400x300")
    Credit(credit_win)
    
    

def Back():
    # take to main page and login
    print("Stuff")
