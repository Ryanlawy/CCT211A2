from tkinter import *
from tkinter import ttk
import csv
import login
from tkinter import messagebox
import database

class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="#25330F")

        # Initialize search variable and search type variable
        self.search_var = StringVar()
        self.search_type_var = StringVar()

        # UI setup
        self.setup_ui()
        # book frame set up
        self.set_bookframe()
        self.set_userframe()

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

        # Search Instruction Label
        self.search_instruction_label = Label(self.search_frame, text="List of Books:", font=("Impact", 20), bg="#25330F", fg="white")
        self.search_instruction_label.grid(row=10, column=1, padx=10, sticky=W)
        self.search_instruction_label.grid(row=10, column=1, padx=10, sticky=W)
        # Display the book list automatically
        self.set_bookframe()

    # populate the list of books
    def set_bookframe(self):
        self.TableMargin = Frame(self.root, bg="#25330F")
        self.TableMargin.pack(side=BOTTOM)
        self.scrollbarx = Scrollbar(self.TableMargin, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.TableMargin, orient=VERTICAL)
        self.tree = ttk.Treeview(self.TableMargin, columns=("bookid", "title", "rating", "language_code", "num_pages", "publication_date", "publisher"), height=400, selectmode="extended", yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('bookid', text="BookID", anchor=W)
        self.tree.heading('title', text="Title", anchor=W)
        self.tree.heading('rating', text="Average Rating", anchor=W)
        self.tree.heading('language_code', text="Language", anchor=W)
        self.tree.heading('num_pages', text="Pages", anchor=W)
        self.tree.heading('publication_date', text="Publication Date", anchor=W)
        self.tree.heading('publisher', text="Publisher", anchor=W)

        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=200)
        self.tree.column('#2', stretch=NO, minwidth=0, width=200)
        self.tree.pack()

        # populate the treeview from a csv
        with open("books.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                bookid = row['bookID']
                title = row['title']
                rating = row['average_rating']
                isbn = row['isbn']
                language = row['language_code']
                page = row['  num_pages']
                date = row['publication_date']
                publisher = row['publisher']
                self.tree.insert("", 0, values=(bookid, title, rating, isbn, language, page, date, publisher))
        self.tree.pack(fill=X)

    # populate the list of users
    def set_userframe(self):
        self.TableMargin = Frame(self.root, bg="#25330F")
        self.TableMargin.pack(side=BOTTOM)
        self.scrollbarx = Scrollbar(self.TableMargin, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.TableMargin, orient=VERTICAL)
        self.tree = ttk.Treeview(self.TableMargin, columns=("userid", "name", "gender", "time", "quote", "author", "tags", "likes"), height=400, selectmode="extended", yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('userid', text="UserID", anchor=W)
        self.tree.heading('name', text="Name", anchor=W)
        self.tree.heading('gender', text="Gender", anchor=W)
        self.tree.heading('time', text="Reading Time ", anchor=W)
        self.tree.heading('quote', text="Favorite Quote", anchor=W)
        self.tree.heading('author', text="Favorite Author", anchor=W)
        self.tree.heading('tags', text="Tags", anchor=W)
        self.tree.heading('likes', text="Likes", anchor=W)

        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=200)
        self.tree.column('#2', stretch=NO, minwidth=0, width=200)
        self.tree.pack()

        # populate the treeview from a csv
        with open("data.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                name = row['\ufeffNames']
                gender = row['Gender']
                time = row['Count']
                self.tree.insert("", 0, values=(name, gender, time))

        with open("quotes.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                userid = row['index']
                quote = row['quote']
                author = row['author']
                tags = row['tags']
                likes = row['likes']
                self.tree.insert("", 0, values=(userid, quote, author, tags, likes))

        self.tree.pack(fill=X)
