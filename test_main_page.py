from tkinter import *
import login
import menus
import main_page
import database
from main_page import MainPage  # Make sure this matches the name of your file and class

def test_main_page():

    main_root = Tk()
    main_root.title("Main Application")
    width = main_root.winfo_screenwidth()
    height = main_root.winfo_screenheight()
    main_root.geometry("%dx%d" % (width, height))
    main_root.resizable(False, True)

    # Initialize the main application interface
    main_page.MainPage(main_root)

    # Initialize menus for the main application, if needed
    menus.makemenu(main_root)
    main_root.mainloop()

if __name__ == "__main__":
    test_main_page()
