from tkinter import *
import login
import menus
"""
# header
# scoler
"""
# run the whole thing


def main():
    root = Tk()
    root.title("Drama BookClub")
    root.geometry("1400x930+100+50")
    root.resizable(False, True)

    #starting the System
    login.Login(root)

    # creating menu
    menus.makemenu(root)

    root.mainloop()


if __name__ == '__main__':
    main()
