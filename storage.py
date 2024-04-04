import shelve
import sqlite3
import tkinter as tk
import meeting


class Storage:
    FILENAME = "callfor.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.FILENAME)
        self.access = self.conn.cursor()

    def get_record(self, rid):
        # dont quite understand this part so just copy it
        self.access.execute(
            """SELECT * from call_meeting WHERE meeting_id = ?;""", (rid,))
        row = self.access.fetchone()
        call_meeting = Meeting(row[1], row[2], row[3], row[4], row[5],
                               row[6], row[7], row[0])
        return call_meeting

    def get_all(self):
        """get all record in the file"""
        self.access.execute("""SELECT * from call_meeting;""")

        call_meeting = []
        for row in self.access:
            call_meeting.append(
                Meeting(row[1], row[2], row[3], row[4], row[5],
                        row[6], row[7], row[0]))
        return call_meeting

    def save(self, record):
        """add a record with a new id"""
        # if it's still 0 then it's a new record, otherwise it's not
        if record.rid == 0:
            self.access.execute("""INSERT INTO call_meeting(username,date,time,
            place,theme,book_selection,email) VALUES (?,?,?,?,?,?,?)
            """, (record.username, record.date, record.time,
                  record.place, record.theme, record.book_selection,
                  record.email))
            record.rid = self.access.lastrowid
        else:
            self.access.execute("""UPDATE call_meeting SET username = ?, 
            date = ?, time = ?, place = ?, theme = ?, book_selection = ?, email = ?
            WHERE meeting_id = ?""", (record.username, record.date, record.time,
                                      record.place, record.theme, record.book_selection,
                                      record.email, record.rid))
        self.conn.commit()

    def get_all_sorted_records(self):
        """get all sorted data"""
        return sorted(self.get_all(), key=lambda x: x.rid)

    def delete_record(self, rid):
        """delete the data"""
        self.access.execute("""DELETE FROM call_meeting WHERE meeting_id = ?""",
                                 (int(rid),))
        self.conn.commit()

    def cleanup(self):
        """close the data struct"""
        if (self.access):
            self.conn.commit()
            self.access.close()


class Meeting:
    """the data structure of a meeting"""
    def __init__(self, username="", date="", time="", place="", theme="",
                 book_selection="", email="", rid=0):
        self.rid = rid
        self.username = username
        self.date = date
        self.time = time
        self.place = place
        self.theme = theme
        self.book_selection = book_selection
        self.email = email

    def __str__(self):
        return f'Contact#: {self.rid}; UserName: {self.username}, DATE: {self.date}, ' \
               f'Time: {self.time}, Meeting Place:{self.place}, Theme: {self.theme}, ' \
               f'Book Selection: {self.book_selection}, Email: {self.email}'


class BookStorage:
    FILENAME = "booklist.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.FILENAME)
        self.access = self.conn.cursor()

    def get_record(self, rid):
        # dont quite understand this part so just copy it
        self.access.execute(
            """SELECT * from booklist WHERE book_list = ?;""", (rid,))
        row = self.access.fetchone()
        book_list = MyList(row[1], row[2], row[3], row[4], row[5],
                               row[6], row[7], row[0])
        return book_list

    def get_all(self):
        """get all record in the file"""
        self.access.execute("""SELECT * from book_list;""")

        book_list = []
        for row in self.access:
            book_list.append(
                MyList(row[1], row[2], row[3], row[4], row[5],
                        row[6], row[7], row[0]))
        return book_list

    def save(self, record):
        """add a record with a new id"""
        # if it's still 0 then it's a new record, otherwise it's not
        if record.rid == 0:
            self.access.execute("""INSERT INTO book_list(bookid,date,time,
            place,theme,book_selection,email) VALUES (?,?,?,?,?,?,?)
            """, (record.bookid, record.title, record.rating,
                  record.language_code, record.num_pages, record.publication_date,
                  record.publisher))
            record.rid = self.access.lastrowid
        else:
            self.access.execute("""UPDATE booklist SET bookid = ?, 
            title = ?, rating = ?, language_code = ?, num_pages = ?, publication_date = ?, publisher = ?
            WHERE list_id = ?""", (record.bookid, record.title, record.rating,
                                      record.language_code, record.num_pages, record.publication_date,
                                      record.publisher, record.rid))
        self.conn.commit()

    def get_all_sorted_records(self):
        """get all sorted data"""
        return sorted(self.get_all(), key=lambda x: x.rid)

    def delete_record(self, rid):
        """delete the data"""
        self.access.execute("""DELETE FROM booklist WHERE list_id = ?""",
                            (int(rid),))
        self.conn.commit()

    def cleanup(self):
        """close the data struct"""
        if (self.access):
            self.conn.commit()
            self.access.close()



class MyList():
    def __init__(self, bookid="", title="", rating="", language_code="", num_pages="",
                 publication_date="", publisher="", rid=0):
        self.rid = rid
        self.bookid = bookid
        self.title = title
        self.rating = rating
        self.language_code = language_code
        self.num_pages = num_pages
        self.publication_date = publication_date
        self.publisher = publisher

    def __str__(self):
        return f'Contact#: {self.rid}; BookID: {self.bookid}, Title: {self.title}, ' \
               f'Average Rating: {self.rating}, Language:{self.language_code}, Pages: {self.num_pages}, ' \
               f'Publication Date: {self.publication_date}, Publisher: {self.publisher}'
