from tkinter import *
from tkinter import ttk
import csv
import login
from tkinter import messagebox
import database
import meeting

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

    def basic_info(self):
        # Your basic info implementation
        pass

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

        self.search_result_label = Label(self.search_frame, text="", font=("Times New Roman", 12), bg="#25330F", fg="white")
        self.search_result_label.grid(row=2, column=1, columnspan=2, padx=10, sticky=W)

        # Search Instruction Label
        self.search_instruction_label = Label(self.search_frame, text="Search books:", font=("Impact", 20), bg="#25330F", fg="white")
        self.search_instruction_label.grid(row=0, column=1, padx=10, sticky=W)

        # Search Entry
        self.search_entry = Entry(self.search_frame, textvariable=self.search_var, font=("Times New Roman", 15), width=50)
        self.search_entry.grid(row=1, column=1, padx=5, sticky=W)

        # Search Button
        self.search_button = Button(self.search_frame, text="Search", command=self.perform_search, fg="black", bg="#25330F", width=10, font=("Impact", 15))
        self.search_button.grid(row=1, column=2, padx=5, sticky=W)

        #  show book Button
        self.showbook_button = Button(self.search_frame, text="All Books",
                                      fg="black", bg="#25330F", width=10,
                                      font=("Impact", 15), command=self.set_book_complex)
        self.showbook_button.grid(row=1, column=3, padx=5, sticky=W)
        # show user button

        self.showuser_button = Button(self.search_frame, text="All Users",
                                      fg="black", bg="#25330F", width=10,
                                      font=("Impact", 15), command=self.set_userframe)
        self.showuser_button.grid(row=1, column=4, padx=5, sticky=W)
        # self.search_type_combobox = ttk.Combobox(self.search_frame, textvariable=self.search_type_var, state="readonly", width=15, style='Custom.TCombobox')
        # self.search_type_combobox['values'] = ('Book', 'User')
        # self.search_type_combobox.current(0)
        # self.search_type_combobox.grid(row=1, column=3, padx=1, sticky=W)
        # self.search_type_combobox.bind("<<ComboboxSelected>>", self.selection_changed(self.search_type_combobox))


        #call for meeting
        self.meeting_button = Button(text="Meeting", command=meeting.FloatScreen, fg="black", bg="#25330F", width=10, font=("Impact", 15))
        #self.meeting_button.grid(row=2, column=2, padx=5, sticky=W)
        self.meeting_button.pack(side="top", padx=10, pady=10)

        #my list
        self.list_button = Button(text="My Lists", command=meeting.FloatScreen, fg="black", bg="#25330F", width=10, font=("Impact", 15))
        #self.list_button.grid(row=2, column=4, padx=5, sticky=W)
        self.list_button.pack(side="top", padx=20, pady=10)


        # # Display the book list automatically
        self.set_bookframe()


    # helper
    def set_book_complex(self):
        try:
            self.TableMargin.destroy()
            self.search_results_frame.destroy()
            self.set_bookframe()
        except:
            self.set_bookframe()



    # populate the list of
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

        self.TableMargin.destroy()
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

        with open("quotes.csv", encoding='utf-8') as t:
            reader = csv.DictReader(t, delimiter=',')
            for row in reader:
                userid = row['index']
                quote = row['quote']
                author = row['author']
                tags = row['tags']
                likes = row['likes']
                self.tree.insert("", 0, values=(userid, quote, author, tags, likes))

    def perform_search(self):
        query = self.search_var.get().lower()  # Convert query to lowercase for case-insensitive search
        search_type = self.search_type_var.get()  # Determine the search type

        # Initialize an empty list for search results
        search_results = []
        # Open and read the CSV file
        with open("books.csv", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Add conditions for searching by different attributes
                if query in row['title'].lower():
                    search_results.append(row)
                # Add more conditions as needed

        # Update the TreeView with the search results
        self.update_booklist(search_results)


    def update_booklist(self, search_results):
        # First, clear any existing search results frame if it exists
        self.TableMargin.destroy()
        if hasattr(self, 'search_results_frame'):
            self.search_results_frame.destroy()

        # Create a new frame for the search results
        self.search_results_frame = Frame(self.root, bg="#25330F")
        self.search_results_frame.pack(fill=BOTH, expand=True)

        # Add scrollbars and Treeview to the search results frame
        scrollbarx = Scrollbar(self.search_results_frame, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.search_results_frame, orient=VERTICAL)
        self.tree = ttk.Treeview(self.search_results_frame, columns=("bookid", "title", "rating", "language_code", "num_pages", "publication_date", "publisher"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        # Define the tree headings and columns
        self.tree.heading('bookid', text="BookID", anchor=W)
        self.tree.heading('title', text="Title", anchor=W)
        # Add the rest of your headings here...

        self.tree.column('#0', stretch=NO, minwidth=0, width=0)


        self.tree.pack(fill=BOTH, expand=True)

        # Clear existing entries in the TreeView
        self.tree.delete(*self.tree.get_children())

        # Insert new search results into the TreeView
        for result in search_results:
            self.tree.insert("", "end", values=(
                result['bookID'], result['title'], result['average_rating'],
                result['language_code'], result['  num_pages'],
                result['publication_date'], result['publisher']))

        # Update the search result label
        self.search_result_label.config(text=f"Number of search results: {len(search_results)}")

        # handle the case where no results are found
        if not search_results:
            self.search_result_label.config(text="No results found.")




