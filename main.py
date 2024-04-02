from tkinter import *
import login
import menus
import main_page
import database

def open_main_application():
    # Initialize the main application window
    new_root = Tk()
    new_root.title("Main Application")
    new_root.geometry("1400x930+100+50")
    new_root.resizable(False, True)

    # Initialize the main application interface
    app = main_page.MainPage(new_root)

    # Initialize menus for the main application, if needed
    menus.makemenu(new_root)

    new_root.mainloop()

def main():
    root = Tk()
    root.title("Drama BookClub")
    root.geometry("300x250")  # Size of the login window

    login_app = login.Login(root, on_success=open_main_application)

    root.mainloop()

if __name__ == '__main__':
    main()

### MVC
### python object model


