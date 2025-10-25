# models.py
from db import conn, cursor

def add_book(title, author, year, isbn):
    cursor.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)",
                   (title, author, year, isbn))
    conn.commit()

def view_books():
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()

def search_books(title="", author="", year="", isbn=""):
    cursor.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",
                   (title, author, year, isbn))
    return cursor.fetchall()

def update_book(book_id, title, author, year, isbn):
    cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",
                   (title, author, year, isbn, book_id))
    conn.commit()

def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()