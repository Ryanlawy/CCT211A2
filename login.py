from tkinter import *
from tkinter import messagebox
import main_page

class Login:
    def __init__(self, root, on_success=None):  # Accept a callback function
        self.root = root
        self.on_success = on_success  # Store the callback

        self.username = StringVar()
        self.password = StringVar()

        # Set the background color
        self.root.config(bg="#25330F")
        self.loginControlFrame()

    # Method to handle the login functionality
    def loginFunc(self):
        # CCT211Awesome
        if self.txtUsername.get() == '12345678' and self.txtPassword.get() == '12345678':
            # If login is successful and a callback function is provided, call it

            messagebox.showinfo("Success", "Login Successful!")
            # Optionally close the login window if no further action is defined
            self.root.destroy()
        else:
            messagebox.showerror("Error!", "Username or password incorrect")
            self.username.set("")
            self.password.set("")

    # Method to create the login interface
    def loginControlFrame(self):
        # Login Frame
        self.loginFrame = Frame(self.root, bg="white")
        self.loginFrame.pack(side=LEFT, fill=X, padx=60)

        # Header above login Box
        self.login_frame_title = Label(self.loginFrame, text="Welcome! Book Lovers!", font=("Impact", 35), bg="white", fg="#25330F")
        self.login_frame_title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
        self.login_frame_title = Label(self.loginFrame, text="Login Below", font=("Impact", 20), bg="white", fg="#25330F")
        self.login_frame_title.grid(row=1, columnspan=2, padx=20, pady=10, sticky="w")

        # Username
        self.labelUsername = Label(self.loginFrame, text="Username", font=("Times New Roman", 16, "bold"), bg="white", fg="#25330F")
        self.labelUsername.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.txtUsername = Entry(self.loginFrame, textvariable=self.username, font=("Times New Roman", 15), width=30)
        self.txtUsername.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Password
        self.labelPassword = Label(self.loginFrame, text="Password", font=("Times New Roman", 16, "bold"), bg="white", fg="#25330F")
        self.labelPassword.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.txtPassword = Entry(self.loginFrame, textvariable=self.password, font=("Times New Roman", 15), width=30, show="*")
        self.txtPassword.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Login Button
        self.Login_button = Button(self.loginFrame, command=self.loginFunc, text="Login", fg="white", bg="#25330F", width=10, font=("Impact", 15))
        self.Login_button.grid(row=5, column=1, padx=10, sticky="e")

        # Right Side Frame (Optional Decorative Frame)
        self.rightFrame = Frame(self.root, bg="#25330F")
        self.rightFrame.pack(side=RIGHT)

        self.labelCompanyName = Label(self.rightFrame, text="Drama BookClub", font=("Goudy Old Style", 55), bg="#25330F", fg="white")
        self.labelCompanyName.pack(pady=20)

        self.labelDesc = Label(self.rightFrame, text="Find Books of all things Beautiful and Lofty!", font=("Times New Roman", 25, "italic"), bg="#25330F", fg="white")
        self.labelDesc.pack()

