import tkinter as tk
from tkinter import *
import tkinter.messagebox as mb
from login import Login
import main_page
import main


def makemenu(win):
    top_menu = tk.Menu(win)  # win=top-level window
    menu = Menu(top_menu, name='name')
    menu.add_command(label="Crew and Credit", command=show_text)
    top_menu.add_cascade(label="Drama BookClub", menu=menu)



    # create a pulldown menu, and add it to the menu bar
    filemenu = Menu(top_menu, tearoff=0)
    filemenu.add_command(label="Logout", command=lambda: to_login(win))
    filemenu.add_command(label="Exit", command=win.quit)

    top_menu.add_cascade(label="View", menu=filemenu)

    # Navigate menus
    nevmenu = Menu(top_menu, tearoff=0)
    nevmenu.add_command(label="Back", command=lambda: to_login(win))
    top_menu.add_cascade(label="Navigate", menu=nevmenu)

    helpmenu = Menu(top_menu, tearoff=0)
    helpmenu.add_command(label="About", command=show_text)
    top_menu.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    win.config(menu=top_menu)



def to_login(win):
    win.destroy()  # This destroys the current window
    main.main()


def show_text():
    info_window = tk.Toplevel()
    info_window.title("Reference")
    # Set the background color of the window
    info_window.configure(bg='#25330F')  # Light gray background

    # Adjust the Label widgets to have the same background color
    tk.Label(info_window, text="Reference:", font=('Times New Roman', 40, 'bold')).pack(pady=10)
    info_text = """CCT211 Week11 code, 
    
    GitHub: https://github.com/HansiKR/Python-tkinter-Project/tree/master"""
    tk.Label(info_window, text=info_text, justify='left').pack(padx=10, pady=10)
    tk.Label(info_window, text="Reference:", font=('Times New Roman', 40, 'bold')).pack(pady=100)
    info_text = """Sean Kao, 
    
    Lai Wei Yu"""
    tk.Label(info_window, text=info_text, justify='left').pack(padx=10, pady=100)


