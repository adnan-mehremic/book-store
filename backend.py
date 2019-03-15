import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book "
                "(id INTEGER PRIMARY KEY, title text, author text, year integer, publication text)")
    conn.commit()
    conn.close()


def insert(title, author, year, publication):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, publication))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", publication=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR publication=?",
                (title, author, year, publication))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id_row):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id_row,))
    conn.commit()
    conn.close()


def update(id_row, title, author, year, publication):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, publication=? WHERE id=?",
                (title, author, year, publication, id_row))
    conn.commit()
    conn.close()


connect()
