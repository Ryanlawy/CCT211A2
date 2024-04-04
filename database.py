import sqlite3

def connect_database():
    global conn, cur

    # will connect to db if exists, or create a new one.
    conn = sqlite3.connect('callfor.db')

    cur = conn.cursor()


def create_database():
    cur.execute('''DROP TABLE IF EXISTS "call_meeting";''')
    cur.execute('''CREATE TABLE IF NOT EXISTS "call_meeting" (
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
    cur.execute('''DROP TABLE IF EXISTS "call_meeting";''')
    cur.execute('''CREATE TABLE IF NOT EXISTS "call_meeting" (
            "meeting_id"	INTEGER PRIMARY KEY,
            "username"	TEXT NOT NULL,
            "date"	TEXT NOT NULL,
            "time"	TEXT NOT NULL,
            "place"	TEXT NOT NULL,
            "theme"	TEXT NOT NULL,
            "book_selection" TEXT NOT NULL,
            "email"	TEXT NOT NULL
            );''')

def close_database():
    conn.commit()
    conn.close()




if __name__ == '__main__':
    connect_database()
    create_database()
    close_database()
