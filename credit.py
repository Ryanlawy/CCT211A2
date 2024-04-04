from tkinter import *
from tkinter import messagebox

class Credit:
    def __init__(self, root):
        self.root = root
        self.username = StringVar()
        self.password = StringVar()
        self.root.config(bg="#25330F")
        self.loginControlFrame()

    def loginControlFrame(self):
        self.loginFrame = Frame(self.root, bg="white")
        self.loginFrame.pack(side=LEFT, fill=X, padx=60)

        # Login interface setup (omitted for brevity)...

        # Adding a credit label to the right side frame
        self.rightFrame = Frame(self.root, bg="#25330F")
        self.rightFrame.pack(side=LEFT, fill=Y)

        self.labelCompanyName = Label(self.rightFrame, text="Drama BookClub", font=("Goudy Old Style", 55), bg="#25330F", fg="white")
        self.labelCompanyName.pack(pady=(10, 0))

        self.labelDesc = Label(self.rightFrame, text="CCT211 Assignment 2", font=("Times New Roman", 25, "italic"), bg="#25330F", fg="white")
        self.labelDesc.pack(pady=(6, 20))

        # Credit Label
        self.labelCredit = Label(self.rightFrame, text="Sean Kao and Lai WeiYu credit", font=("Times New Roman",20), bg="#25330F", fg="white")
        self.labelCredit.pack(side=BOTTOM, pady=(1, 1))

        # Adding a credit label to the right side frame
        self.leftFrame = Frame(self.root, bg="#25330F")
        self.leftFrame.pack(side=TOP, fill=Y)

        self.labelCompanyName = Label(self.leftFrame, text="Reference", font=("Goudy Old Style", 55), bg="#25330F", fg="white")
        self.labelCompanyName.pack(pady=(10, 0))

        self.labelDesc = Label(self.leftFrame, text="CCT211 demo code", font=("Times New Roman", 25, "italic"), bg="#25330F", fg="white")
        self.labelDesc.pack(pady=(6, 20))
        self.labelDesc = Label(self.leftFrame, text="CCT211 demo code", font=("Times New Roman", 25, "italic"), bg="#25330F", fg="white")
        self.labelDesc.pack(pady=(6, 20))
        self.labelDesc = Label(self.leftFrame, text="CCT211 demo code", font=("Times New Roman", 25, "italic"), bg="#25330F", fg="white")
        self.labelDesc.pack(pady=(6, 20))


# Test the Credit class
if __name__ == "__main__":
    root = Tk()
    root.title("Drama BookClub Login")
    root.geometry("800x400")  # Adjust the size of the window as needed
    app = Credit(root)
    root.mainloop()





