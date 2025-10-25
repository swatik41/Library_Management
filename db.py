# db.py
import sqlite3

# Connect to SQLite database (it will create library.db if it doesn't exist)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create the books table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    isbn TEXT UNIQUE
)
""")

# Commit changes
conn.commit()