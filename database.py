import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('books.csv')
        except Error:
            print("Cannot Load Database")

        self.cur = self.conn.cursor()

        booksq = """
            CREATE TABLE IF NOT EXISTS Book_list (
            bookID Integer PRIMARY KEY,
            title text,
            average_rating text,
            isbn text,
            num_pages Integer,
            ratings_count Integer,
            text_reviews_count Integer,
            publication_date text,
            publisher text,
            )
            """

        usersq = """
            CREATE TABLE IF NOT EXISTS User_list (
            userID Integer PRIMARY KEY,
            name text,
            gender text,
             text,
            telNo text,
            hrRate real,
            availability text,
            availableDays text,
            username text,
            password text
            )
        """

        reviewsq = """
            CREATE TABLE IF NOT EXISTS User_list (
            userID Integer PRIMARY KEY,
            name text,
            gender text,
            Count text,
            Probability text
            )
        """

        self.cur.execute(booksq)
        self.cur.execute(usersq)
        self.cur.execute(reviewsq)
        self.conn.commit()


