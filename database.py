from tkinter import *
import tkinter.ttk as ttk
import csv


# set up the screen
root = Tk()
root.title("BOOKS")
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#set up the treeview
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("bookid", "title", "rating", "language_code", "num_pages", "publication_date", "publisher"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('bookid', text="BookID", anchor=W)
tree.heading('title', text="Title", anchor=W)
tree.heading('rating', text="Average Rating", anchor=W)
tree.heading('language_code', text="Language", anchor=W)
tree.heading('num_pages', text="Pages", anchor=W)
tree.heading('publication_date', text="Publication Date", anchor=W)
tree.heading('publisher', text="Publisher", anchor=W)

tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.pack()

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

        tree.insert("", 0, values=(bookid, title, rating, isbn, language, page, date, publisher))

#
# TableMargin = Frame(root, bg="#25330F")
# TableMargin.pack(side=BOTTOM)
# scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
# scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
# tree = ttk.Treeview(TableMargin, columns=("userid", "name", "gender", "time", "quote", "author", "tags", "likes"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
# scrollbary.config(command=tree.yview)
# scrollbary.pack(side=RIGHT, fill=Y)
# scrollbarx.config(command=tree.xview)
# scrollbarx.pack(side=BOTTOM, fill=X)
# tree.heading('userid', text="UserID", anchor=W)
# tree.heading('name', text="Name", anchor=W)
# tree.heading('gender', text="Gender", anchor=W)
# tree.heading('time', text="Reading Time ", anchor=W)
# tree.heading('quote', text="Favorite Quote", anchor=W)
# tree.heading('author', text="Favorite Author", anchor=W)
# tree.heading('tags', text="Tags", anchor=W)
# tree.heading('likes', text="Likes", anchor=W)
#
# tree.column('#0', stretch=NO, minwidth=0, width=0)
# tree.column('#1', stretch=NO, minwidth=0, width=200)
# tree.column('#2', stretch=NO, minwidth=0, width=200)
# tree.pack()
#
# # populate the treeview from a csv
# with open("data.csv", encoding='utf-8') as f:
#     reader = csv.DictReader(f, delimiter=',')
#     for row in reader:
#         name = row['Name']
#         gender = row['Gender']
#         time = row['Count']
#         tree.insert("", 0, values=(name, gender, time))
#
# with open("quotes.csv", encoding='utf-8') as f:
#     reader = csv.DictReader(f, delimiter=',')
#     for row in reader:
#         userid = row['index']
#         quote = row['quote']
#         author = row['author']
#         tags = row['tags']
#         likes = row['likes']
#         tree.insert("", 0, values=(userid, quote, author, tags, likes))
#
# tree.pack(fill=X)

if __name__ == '__main__':
     root.mainloop()
