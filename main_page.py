from tkinter import *
from tkinter import ttk


class MainPage:
    def __init__(self, root):
        self.root = root

        self.username = StringVar()
        self.password = StringVar()

        # Background Color
        self.root.config(bg="#25330F")

    def basic_info(self):

        self.main_frame = Frame(self.root, bg="#25330F")
        self.main_frame.pack(side=TOP, fill=X)
        self.main_frame_title = Label(self.main_frame, text="Basic Info Page", font=("Times New Roman", 35),
                                      bg="#25330F", fg="white")

        self.main_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
        # Student Full Name
        self.labelStName = Label(self.main_frame, text="Student Name", font=("Times New Roman", 16, "bold"),
                                 bg="#5856a0",
                                 fg="white")
        self.labelStName.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txtStName = Entry(self.main_frame, textvariable=self.studentName, font=("Times New Roman", 15), width=30,
                               state="readonly")
        self.txtStName.grid(row=1, column=1, padx=10, pady=5, sticky="w")
