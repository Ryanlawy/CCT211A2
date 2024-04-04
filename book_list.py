import tkinter as tk
from tkinter import font as tkfont
import tkinter.ttk as ttk
import storage
from tkinter import messagebox
import main_page

"""
the similar modual to create a window to adding deleting book object for request
"""

class ListScreen(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.data = storage.BookStorage()
        self.title_font = tkfont.Font(
            family='Times', size=12, weight="bold", slant="italic")

        # frame stacks
        stack = tk.Frame(self)
        stack.pack(side="top", fill="both", expand=True)
        stack.grid_rowconfigure(0, weight=1)
        stack.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainFrame, ReadFrame, AddBook):
            data_name = F.__name__
            frame = F(parent=stack, controller=self, persist=self.data)
            self.frames[data_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainFrame")

    def show_frame(self, page, rid=0):
        """Show the frame"""
        frame = self.frames[page]
        if not rid == 0:
            frame.update(rid)
        else:
            frame.update()
        frame.tkraise()

    def get_page(self):
        return self.frames["MainFrame"]


class MainFrame(tk.Frame):
    """allow viewing, deleting, adding in the main frame"""

    def __init__(self, parent, controller, persist=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Request Book List",
                         font=controller.title_font)
        label.grid(column=0, pady=10)

        # treeview
        contact_table = tk.Frame(self, width=500)
        contact_table.grid(column=0)
        scrollbarx = tk.Scrollbar(contact_table, orient=tk.HORIZONTAL)
        scrollbary = tk.Scrollbar(contact_table, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(contact_table, columns=("bookid", "title",
                                                         "rating", "language_code", "num_pages", "publication_date", "publisher"),
                                 selectmode="extended", yscrollcommand=scrollbary.set,
                                 xscrollcommand=scrollbarx.set)

        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbarx.config(command=self.tree.xview)
        scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
        #columns
        self.tree.heading('bookid', text="BookID", anchor=tk.W)
        self.tree.heading('title', text="Title", anchor=tk.W)
        self.tree.heading('rating', text="Average Rating", anchor=tk.W)
        self.tree.heading('language_code', text="Language", anchor=tk.W)
        self.tree.heading('num_pages', text="Pages", anchor=tk.W)
        self.tree.heading('publication_date', text="Publication Date", anchor=tk.W)
        self.tree.heading('publisher', text="Publisher", anchor=tk.W)

        self.tree.column('#0', stretch=tk.NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=tk.NO, minwidth=0, width=60)
        self.tree.column('#2', stretch=tk.NO, minwidth=0, width=200)
        self.tree.column('#3', stretch=tk.NO, minwidth=0, width=200)
        self.tree.bind('<<TreeviewSelect>>', self.select)
        self.tree.pack()
        self.selected = []

        self.persist = persist
        all_records = self.persist.get_all_sorted_records()

        for record in all_records:
            self.tree.insert("", 0, values=(
                record.rid, record.bookid, record.title, record.rating,
                record.language_code, record.num_pages, record.publication_date,
                record.publisher))

        edit_button = tk.Button(self, text="Edit Book",
                                command=self.edit_book)
        edit_button.grid(column=0)

        delete_button = tk.Button(self, text="Delete book",
                                  command=self.delete_book)
        delete_button.grid(column=0)

        new_button = tk.Button(self, text="Request New Book",
                               command=lambda: controller.show_frame("AddBook"))
        new_button.grid(column=0)

    def edit_book(self):
        # if there is no book to edit
        try:
            idx = self.selected[0]
            record_id = self.tree.item(idx)['values'][0]
            self.controller.show_frame("ReadFrame", record_id)
        except IndexError:
            # if there is no selected book
            messagebox.showinfo("Oh No ~", "Please Select a Book you want to Edit!")
            self.controller.destroy()


        except:
            messagebox.showinfo("oh No ~", "There's no Book to be Edit, try Calling for one first!")
            self.controller.destroy()

    def select(self, event):
            """highlight the selection"""
            self.selected = event.widget.selection()

    def delete_book(self):
        """deleting selected book"""
        # delect all selection from the list selected
        if len(self.selected) == 0:
            messagebox.showinfo("Oh No ~", "No Book have been selected for delete")
            self.controller.destroy()

        try:
            # a random error check the try statement
            error_test = self.selected[0]
            for idx in self.selected:
                record_id = self.tree.item(idx)['values'][0]
                # remove from file
                self.persist.delete_record(record_id)
                # remove from treeview
                self.tree.delete(idx)
        except:
            messagebox.showinfo("oh No ~", "Can't see any Book to be delete, try Calling for one first!")
            self.controller.destroy()

def update(self):
        """refresh the treeview"""
        for row in self.tree.get_children():
            self.tree.delete(row)
        all_records = self.persist.get_all_sorted_records()
        for record in all_records:
            self.tree.insert("", 0, values=(
                record.rid, record.bookid, record.title, record.rating,
                record.language_code, record.num_pages, record.publication_date,
                record.publisher))


class ReadFrame(tk.Frame):
    ''' set up as an edit form the same as the create page form
    this is incredibly redundant, refactoring the similar behaviour into a
    separate function would be a key step before adding or changing the form
    '''

    def __init__(self, parent, controller, persist=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Edit",
                         font=controller.title_font)
        label.grid(row=0, column=0)
        # this object is the data persistence model
        self.persist = persist
        # this empty dict will hold each of the data entry fields
        self.data = {}
        """set up the form, and a submit button """
        # username
        self.data['bookid'] = EntryField(self, label='bookid')
        self.data['bookid'].grid(row=1, column=0, pady=2)
        # Date
        self.data['Title'] = EntryField(self, label='Title')
        self.data['Title'].grid(row=2, column=0, pady=2)
        # time
        self.data['Time'] = EntryField(self, label='Time')
        self.data['Time'].grid(row=3, column=0, pady=2)
        # place
        self.data['Average Rating'] = EntryField(self, label='Average Rating')
        self.data['Average Rating'].grid(row=4, column=0, pady=2)

        self.data['Language'] = EntryField(self, label='Language')
        self.data['Language'].grid(row=5, column=0, pady=2)

        self.data['Pages'] = EntryField(self, label='Pages')
        self.data['Pages'].grid(row=6, column=0, pady=2)

        self.data['Publisher'] = EntryField(self, label='Publisher')
        self.data['Publisher'].grid(row=7, column=0, pady=2)

        self.Button1 = tk.Button(self, text='Update',
                                 activeforeground="blue", command=self.submit)
        self.Button1.grid(row=8, column=0, pady=10)

        button = tk.Button(self, text="Return to My BookList",
                           command=lambda: controller.show_frame("MainFrame"))
        button.grid(row=9, column=0)

    def update(self, rid):
        record = self.controller.data.get_record(rid)
        # expand this by adding each of the separate field names
        # or come up with an introspective method (for key in ..)
        self.data['BookID'].dataentry.set(record.username)
        self.data['Title'].dataentry.set(record.date)
        self.data['Average Rating'].dataentry.set(record.time)
        self.data['Language'].dataentry.set(record.place)
        self.data['Pages'].dataentry.set(record.theme)
        self.data['Publication Date'].dataentry.set(record.book_selection)
        self.data['Publisher'].dataentry.set(record.email)

        self.list = self.persist.get_record(rid)
        self.controller.show_frame("MainFrame")

    def submit(self):
        ''' grab the text placed in the entry widgets accessed through the dict
        '''

        self.list.name = self.data['BookID'].get()
        self.list.email = self.data['Title'].get()
        self.list.name = self.data['Average Rating'].get()
        self.list.email = self.data['Language'].get()
        self.list.email = self.data['Pages'].get()
        self.list.name = self.data['Publication Date'].get()
        self.list.email = self.data['Publisher'].get()

        self.persist.save(self.list)
        self.controller.show_frame("MainFrame")


class AddBook(tk.Frame):
    ''' provides a form for creating a new meeting
    '''

    def __init__(self, parent, controller, persist=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Create New BOOK",
                         font=controller.title_font)
        label.grid(row=0, column=0)
        # this object is the data persistence model
        self.persist = persist
        # this empty dict will hold each of the data entry fields
        self.data = {}

        self.data['bookid'] = EntryField(self, label='bookid')
        self.data['bookid'].grid(row=1, column=0, pady=2)

        self.data['title'] = EntryField(self, label='title')
        self.data['title'].grid(row=2, column=0, pady=2)

        self.data['rating'] = EntryField(self, label='Rating')
        self.data['rating'].grid(row=3, column=0, pady=2)

        self.data['language_code'] = EntryField(self, label='Meeting Place')
        self.data['language_code'].grid(row=4, column=0, pady=2)

        self.data['num_pages'] = EntryField(self, label='Theme')
        self.data['num_pages'].grid(row=5, column=0, pady=2)

        self.data['publication_date'] = EntryField(self, label='Book Selection')
        self.data['publication_date'].grid(row=6, column=0, pady=2)

        self.data['publisher'] = EntryField(self, label='Email')
        self.data['publisher'].grid(row=7, column=0, pady=2)

        self.Button1 = tk.Button(self, text='Submit', activebackground="green",
                                 activeforeground="blue", command=self.submit)
        self.Button1.grid(row=8, column=0, pady=10)

        button = tk.Button(self, text="Return to the browse page",
                           command=lambda: controller.show_frame("MainFrame"))
        button.grid(row=9, column=0)

    def reset(self):
        """reset the frame"""
        for key in self.data:
            self.data[key].reset()

    def update(self):
        self.reset()

    def submit(self):
        """create a new meeting base on the form"""
        c = storage.MyList(bookid=self.data['bookid'].get(),
                               title=self.data['title'].get(),
                      rating=self.data['rating'].get(),
                      language_code=self.data['language_code'].get(),
                      num_pages=self.data['num_pages'].get(),
                      publication_date=self.data['publication_date'].get(),
                      publisher=self.data['publisher'].get()
                       )

        self.persist.save(c)
        self.update()
        self.controller.show_frame("MainFrame")


class EntryField(tk.Frame):
    def __init__(self, parent, label='', passwordField=False, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.dataentry = tk.StringVar()
        self.label = label

        self.title = tk.Label(self, text=label, width=10)
        self.title.grid(row=0, column=0, padx=10, sticky=(tk.W + tk.E))

        if passwordField:
            self.field = tk.Entry(
                self, width=30, textvariable=self.dataentry, show="*")
        else:
            self.field = tk.Entry(
                self, width=30, textvariable=self.dataentry)
        self.field.grid(row=0, column=1, padx=15, sticky=(tk.W + tk.E))

    def reset(self):
        self.dataentry.set("")

    def get(self):
        return self.dataentry.get()


if __name__ == "__main__":
    app = ListScreen()
    app.mainloop()
