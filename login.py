from tkinter import *
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root = root

        self.username = StringVar()
        self.password = StringVar()

        # Background Color
        self.root.config(bg="#25330F")
        self.loginControlFrame()

    # login method to go to the next frames
    def loginFunc(self):
        if self.txtUsername.get() == 'lavey' and self.txtPassword.get() == '12345':
            self.loginFrame.destroy()
            self.rightFrame.destroy()
        else:
            messagebox.showerror("Error!", "Usrename or password incorrect")
            self.username.set("")
            self.password.set("")

    """Login Box"""
    def loginControlFrame(self):
        # Login Frame
        self.loginFrame = Frame(self.root, bg="white")
        self.loginFrame.pack(side=LEFT, fill=X, padx=60)
        # Header above login Box
        self.login_frame_title = Label(self.loginFrame, text="Welcome! Book Lovers! ", font=("Impact", 35), bg="white",
                                       fg="#25330F")
        self.login_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
        self.login_frame_title = Label(self.loginFrame, text="Login Below", font=("Impact", 20), bg="white",
                                       fg="#25330F")
        self.login_frame_title.grid(row=1, columnspan=2, padx=20, pady=10, sticky="w")

        # Username
        self.labelUsername = Label(self.loginFrame, text="Username", font=("Times New Roman", 16, "bold"), bg="white",
                                   fg="#25330F")
        self.labelUsername.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.txtUsername = Entry(self.loginFrame, textvariable=self.username, font=("Times New Roman", 15), width=30,)
        self.txtUsername.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Password
        self.labelPassword = Label(self.loginFrame, text="Password", font=("Times New Roman", 16, "bold"), bg="white",
                                   fg="#25330F")
        self.labelPassword.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.txtPassword = Entry(self.loginFrame, textvariable=self.password, font=("Times New Roman", 15), width=30,
                                 bd=5, show="*")
        self.txtPassword.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Login Button
        self.Login_button = Button(self.loginFrame, command=self.loginFunc, text="Login",
                               fg="white", bg="#25330F", width=10, font=("Impact", 15))
        self.Login_button.grid(row=5, column=1, padx=10, sticky="e")

        # empty label for spacing in grid
        self.emptyLabel = Label(self.loginFrame, font=("Times New Roman", 16, "bold"), bg="white",
                                fg="#25330F")
        self.emptyLabel.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Right Side Frame
        self.rightFrame = Frame(self.root, bg="#25330F")
        self.rightFrame.pack(side=RIGHT)

        self.labelCompanyName = Label(self.rightFrame, text="Drama BookClub", font=("Goudy Old Style", 55),
                                      bg="#25330F", fg="white")
        self.labelCompanyName.grid(row=0, column=2, columnspan=2, padx=10)

        self.labelDesc = Label(self.rightFrame, text="Find Books of all things Beautiful and Lofty!", font=("Times New Roman", 25, "italic"),
                               bg="#25330F", fg="white")
        self.labelDesc.grid(row=1, column=2, columnspan=2, padx=10, pady=6)
