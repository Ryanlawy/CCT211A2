from tkinter import *
import login
import menus
import main_page
import database

"""
The main function that runs the whole APP
"""

def main():
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.title("Drama BookClub")
    root.geometry("%dx%d" % (width, height))  # Size of the login window

    login.Login(root)
    root.mainloop()

    # bring out the main page
    main_root = Tk()
    main_root.title("Main Application")
    main_root.geometry("%dx%d" % (width, height))
    main_root.resizable(False, True)

    # Initialize the main application interface
    main_page.MainPage(main_root)

    # Initialize menus for the main application
    menus.makemenu(main_root)
    main_root.mainloop()

if __name__ == '__main__':
    main()


