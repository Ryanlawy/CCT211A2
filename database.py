import sqlite3
"""this is the database files that manage and control the csv. data"""
def connect_database():
    global conn1, cur1, conn2, cur2

    # will connect to db if exists, or create a new one.
    conn1 = sqlite3.connect('callfor.db')
    cur1 = conn1.cursor()

    conn2 = sqlite3.connect('booklist.db')
    cur2 = conn2.cursor()


def create_database():
    cur1.execute('''DROP TABLE IF EXISTS "call_meeting";''')
    cur1.execute('''CREATE TABLE IF NOT EXISTS "call_meeting" (
            "meeting_id"	INTEGER PRIMARY KEY,
            "username"	TEXT NOT NULL,
            "date"	TEXT NOT NULL,
            "time"	TEXT NOT NULL,
            "place"	TEXT NOT NULL,
            "theme"	TEXT NOT NULL,
            "book_selection" TEXT NOT NULL,
            "email"	TEXT NOT NULL
            );''')

def create_book_database():
    cur2.execute('''DROP TABLE IF EXISTS "book_list";''')
    cur2.execute('''CREATE TABLE IF NOT EXISTS "book_list" (
            "bookid"	INTEGER PRIMARY KEY,
            "title"	TEXT NOT NULL,
            "rating"	TEXT NOT NULL,
            "language_code"	TEXT NOT NULL,
            "num_pages"	TEXT NOT NULL,
            "publication_date" TEXT NOT NULL,
            "publisher"	TEXT NOT NULL
            );''')

def close_database():
    conn1.commit()
    conn1.close()

    conn2.commit()
    conn2.close()


if __name__ == '__main__':
    connect_database()
    create_database()
    create_book_database()
    close_database()

