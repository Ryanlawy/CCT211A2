from tkinter import *
from tkinter import ttk

class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="#25330F")

        # Initialize search variable and search type variable
        self.search_var = StringVar()
        self.search_type_var = StringVar()

        # UI setup
        self.setup_ui()

    def basic_info(self):
        # Your basic info implementation
        pass

    def perform_search(self):
        # Placeholder for search logic
        query = self.search_var.get()  # Get the current search query
        search_type = self.search_type_var.get()  # Get the selected search type ('Book Name' or 'Author')
        print(f"Searching for: {query} by {search_type}")
        # Implement search logic here

    def setup_ui(self):
        # Basic Info
        self.basic_info()

        # Create a Style
        style = ttk.Style()
        style.theme_use('clam')  # 'clam' is usually a good starting point for customization

        # Configure our custom style
        # Configure our custom style for the Combobox
        style.configure('Custom.TCombobox', foreground='white', background='#25330F', fieldbackground='#25330F', arrowcolor='white')
        # Attempt to style the selection in the dropdown list (results may vary)
        style.map('Custom.TCombobox',
          selectbackground=[('active', '#25330F')],
          selectforeground=[('active', 'white')],
          fieldbackground=[('readonly', '#25330F')])


        # Search Frame
        self.search_frame = Frame(self.root, bg="#25330F")
        self.search_frame.pack(side=TOP, fill=X, pady=20)

        # Configure the grid layout in search_frame
        self.search_frame.columnconfigure(0, weight=1)
        self.search_frame.columnconfigure(1, weight=3)
        self.search_frame.columnconfigure(2, weight=1)
        self.search_frame.columnconfigure(3, weight=1)

        # Search Instruction Label
        self.search_instruction_label = Label(self.search_frame, text="Search books:", font=("Impact", 20), bg="#25330F", fg="white")
        self.search_instruction_label.grid(row=0, column=1, padx=10, sticky=W)

        # Search Entry
        self.search_entry = Entry(self.search_frame, textvariable=self.search_var, font=("Times New Roman", 15), width=50)
        self.search_entry.grid(row=1, column=1, padx=15, sticky=W)

        # Search Button
        self.search_button = Button(self.search_frame, text="Search", fg="black", bg="#25330F", width=10, font=("Impact", 15))
        self.search_button.grid(row=1, column=2, padx=10, sticky=W)

        # Search Type Combobox
        self.search_type_combobox = ttk.Combobox(self.search_frame, textvariable=self.search_type_var, state="readonly", width=15, style='Custom.TCombobox')
        self.search_type_combobox['values'] = ('Book Name', 'Author')
        self.search_type_combobox.current(0)
        self.search_type_combobox.grid(row=1, column=3, padx=1, sticky=W)

