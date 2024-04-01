from tkinter import Tk
from main_page import MainPage  # Make sure this matches the name of your file and class

def test_main_page():
    root = Tk()
    root.geometry("800x600")  # You can adjust the size as needed
    app = MainPage(root)
    root.mainloop()

if __name__ == "__main__":
    test_main_page()
