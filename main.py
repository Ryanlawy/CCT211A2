from tkinter import *
import login
import menus
import main_page
import database

def main():
    root = Tk()
    root.title("Drama BookClub")
    root.geometry("300x250")  # Size of the login window

    login.Login(root, on_success=None)
    root.mainloop()

    # bring out the main page
    main_root = Tk()
    main_root.title("Main Application")
    main_root.geometry("1400x930+100+50")
    main_root.resizable(False, True)

    # Initialize the main application interface
    main_page.MainPage(main_root)

    # Initialize menus for the main application, if needed
    menus.makemenu(main_root)
    main_root.mainloop()

if __name__ == '__main__':
    main()

### MVC
### python object model


