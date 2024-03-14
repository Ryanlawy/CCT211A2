from tkinter import *
from tkinter import ttk


class MainPage:
    def __init__(self, root):
        self.root = root

        self.username = StringVar()
        self.password = StringVar()

        # Background Color
        self.root.config(bg="#25330F")
        self.loginControlFrame()
