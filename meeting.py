import tkinter as tk
from tkinter import font as tkfont
import tkinter.ttk as ttk
import storage
from tkinter import messagebox


"""
This part is used to create the meeting sign-up 
following the structure of demo from class we add a similar feature to our 
application 

In addition to that we add a range of different improvement to the code such as:
jumping back to the main page after submit or update, adding warning messages for
checking if a meeting is selected when editing and deleting, 
pushing warning messages if there are no meeting in the data when deleting and editing
 
"""


class FloatScreen(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.data = storage.Storage()
        self.title_font = tkfont.Font(
            family='Times', size=12, weight="bold", slant="italic")

        # frame stacks
        stack = tk.Frame(self)
        stack.pack(side="top", fill="both", expand=True)
        stack.grid_rowconfigure(0, weight=1)
        stack.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainFrame, ReadFrame, AddFrame):
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

        label = tk.Label(self, text="Meetings",
                         font=controller.title_font)
        label.grid(column=0, pady=10)

        # treeview
        contact_table = tk.Frame(self, width=500)
        contact_table.grid(column=0)
        scrollbarx = tk.Scrollbar(contact_table, orient=tk.HORIZONTAL)
        scrollbary = tk.Scrollbar(contact_table, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(contact_table, columns=("username", "date",
                        "time", "place", "theme", "book_selection", "email"),
                        selectmode="extended", yscrollcommand=scrollbary.set,
                        xscrollcommand=scrollbarx.set)

        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbarx.config(command=self.tree.xview)
        scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
        #columns
        self.tree.heading('username', text="UserName", anchor=tk.W)
        self.tree.heading('date', text="Date", anchor=tk.W)
        self.tree.heading('time', text="Time", anchor=tk.W)
        self.tree.heading('place', text="Meeting Place", anchor=tk.W)
        self.tree.heading('theme', text="Theme", anchor=tk.W)
        self.tree.heading('book_selection', text="Book Selection", anchor=tk.W)
        self.tree.heading('email', text="Email", anchor=tk.W)

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
                record.rid, record.username, record.date, record.time,
                record.place, record.theme, record.book_selection,
                record.email))

        edit_button = tk.Button(self, text="Edit Exiting Meeting",
                                command=self.edit_meeting)
        edit_button.grid(column=0)

        delete_button = tk.Button(self, text="Delete Meeting",
                                  command=self.delete_meeting)
        delete_button.grid(column=0)

        new_button = tk.Button(self, text="Call For New Meeting",
                               command=lambda: controller.show_frame("AddFrame"))
        new_button.grid(column=0)

    def edit_meeting(self):
        # if there is no meeting to edit
        try:
            idx = self.selected[0]
            record_id = self.tree.item(idx)['values'][0]
            self.controller.show_frame("ReadFrame", record_id)
        except IndexError:
            # if there is no selected meeting
            messagebox.showinfo("Oh No ~", "Please Select a Meeting you want to Edit!")

        except:
            messagebox.showinfo("oh No ~", "There's no Meeting to be Edit, try Calling for one first!")

    def select(self, event):
        """highlight the selection"""
        self.selected = event.widget.selection()

    def delete_meeting(self):
        """deleting selected meeting"""
        # delect all selection from the list selected
        if len(self.selected) == 0:
            messagebox.showinfo("Oh No ~", "No Meeting have been selected for delete")
        try:
            error_test = self.selected[0]
            for idx in self.selected:
                record_id = self.tree.item(idx)['values'][0]
                # remove from file
                self.persist.delete_record(record_id)
                # remove from treeview
                self.tree.delete(idx)
        except:
            messagebox.showinfo("oh No ~", "Can't see any Meeting to be delete, try Calling for one first!")

    def update(self):
        """refresh the treeview"""
        for row in self.tree.get_children():
            self.tree.delete(row)
        all_records = self.persist.get_all_sorted_records()
        for record in all_records:
            self.tree.insert("", 0, values=(
                record.rid, record.username, record.date, record.time,
                record.place, record.theme, record.book_selection,
                record.email))


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
        self.data['UserName'] = EntryField(self, label='UserName')
        self.data['UserName'].grid(row=1, column=0, pady=2)
        # Date
        self.data['DATE'] = EntryField(self, label='DATE')
        self.data['DATE'].grid(row=2, column=0, pady=2)
        # time
        self.data['Time'] = EntryField(self, label='Time')
        self.data['Time'].grid(row=3, column=0, pady=2)
        # place
        self.data['Meeting Place'] = EntryField(self, label='Meeting Place')
        self.data['Meeting Place'].grid(row=4, column=0, pady=2)

        self.data['Theme'] = EntryField(self, label='Theme')
        self.data['Theme'].grid(row=5, column=0, pady=2)

        self.data['Book Selection'] = EntryField(self, label='Book Selection')
        self.data['Book Selection'].grid(row=6, column=0, pady=2)

        self.data['Email'] = EntryField(self, label='Email')
        self.data['Email'].grid(row=7, column=0, pady=2)

        self.Button1 = tk.Button(self, text='Update',
                                 activeforeground="blue", command=self.submit)
        self.Button1.grid(row=8, column=0, pady=10)

        button = tk.Button(self, text="Return to Meetings",
                           command=lambda: controller.show_frame("MainFrame"))
        button.grid(row=9, column=0)

    def update(self, rid):
        record = self.controller.data.get_record(rid)
        # expand this by adding each of the separate field names
        # or come up with an introspective method (for key in ..)
        self.data['UserName'].dataentry.set(record.username)
        self.data['DATE'].dataentry.set(record.date)
        self.data['Time'].dataentry.set(record.time)
        self.data['Meeting Place'].dataentry.set(record.place)
        self.data['Theme'].dataentry.set(record.theme)
        self.data['Book Selection'].dataentry.set(record.book_selection)
        self.data['Email'].dataentry.set(record.email)

        self.meeting = self.persist.get_record(rid)
        self.controller.show_frame("MainFrame")

    def submit(self):
        ''' grab the text placed in the entry widgets accessed through the dict
        '''

        self.meeting.name = self.data['UserName'].get()
        self.meeting.email = self.data['DATE'].get()
        self.meeting.name = self.data['Time'].get()
        self.meeting.email = self.data['Meeting Place'].get()
        self.meeting.email = self.data['Theme'].get()
        self.meeting.name = self.data['Book Selection'].get()
        self.meeting.email = self.data['Email'].get()

        self.persist.save(self.meeting)
        self.controller.show_frame("MainFrame")

class AddFrame(tk.Frame):
    ''' provides a form for creating a new meeting
    '''

    def __init__(self, parent, controller, persist=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Create New Meeting",
                         font=controller.title_font)
        label.grid(row=0, column=0)
        # this object is the data persistence model
        self.persist = persist
        # this empty dict will hold each of the data entry fields
        self.data = {}

        self.data['UserName'] = EntryField(self, label='UserName')
        self.data['UserName'].grid(row=1, column=0, pady=2)

        self.data['DATE'] = EntryField(self, label='DATE')
        self.data['DATE'].grid(row=2, column=0, pady=2)

        self.data['Time'] = EntryField(self, label='Time')
        self.data['Time'].grid(row=3, column=0, pady=2)

        self.data['Meeting Place'] = EntryField(self, label='Meeting Place')
        self.data['Meeting Place'].grid(row=4, column=0, pady=2)

        self.data['Theme'] = EntryField(self, label='Theme')
        self.data['Theme'].grid(row=5, column=0, pady=2)

        self.data['Book Selection'] = EntryField(self, label='Book Selection')
        self.data['Book Selection'].grid(row=6, column=0, pady=2)

        self.data['Email'] = EntryField(self, label='Email')
        self.data['Email'].grid(row=7, column=0, pady=2)

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
        c = storage.Meeting(username=self.data['UserName'].get(),
                            date=self.data['DATE'].get(),
                            time=self.data['Time'].get(),
                            place=self.data['Meeting Place'].get(),
                            theme=self.data['Theme'].get(),
                            book_selection=self.data['Book Selection'].get(),
                            email=self.data['Email'].get()
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
    app = FloatScreen()
    app.mainloop()
