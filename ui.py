# ui.py
import tkinter as tk
from tkinter import messagebox
import models

def refresh_listbox():
    listbox.delete(0, tk.END)
    for book in models.view_books():
        listbox.insert(tk.END, book)

def add_book():
    if title_text.get() == "" or author_text.get() == "":
        messagebox.showwarning("Required fields", "Title and Author cannot be empty!")
        return
    models.add_book(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    refresh_listbox()

def delete_book():
    try:
        selected = listbox.curselection()[0]
        book_id = listbox.get(selected)[0]
        models.delete_book(book_id)
        refresh_listbox()
    except IndexError:
        messagebox.showwarning("Select book", "Please select a book to delete")

def update_book():
    try:
        selected = listbox.curselection()[0]
        book_id = listbox.get(selected)[0]
        models.update_book(book_id, title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        refresh_listbox()
    except IndexError:
        messagebox.showwarning("Select book", "Please select a book to update")

def search_books():
    listbox.delete(0, tk.END)
    for book in models.search_books(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        listbox.insert(tk.END, book)

# ---------------- Tkinter window ----------------
window = tk.Tk()
window.title("Library Management System")

# Labels
tk.Label(window, text="Title").grid(row=0, column=0)
tk.Label(window, text="Author").grid(row=0, column=2)
tk.Label(window, text="Year").grid(row=1, column=0)
tk.Label(window, text="ISBN").grid(row=1, column=2)

# Entry fields
title_text = tk.StringVar()
author_text = tk.StringVar()
year_text = tk.StringVar()
isbn_text = tk.StringVar()

tk.Entry(window, textvariable=title_text).grid(row=0, column=1)
tk.Entry(window, textvariable=author_text).grid(row=0, column=3)
tk.Entry(window, textvariable=year_text).grid(row=1, column=1)
tk.Entry(window, textvariable=isbn_text).grid(row=1, column=3)

# Listbox and scrollbar
listbox = tk.Listbox(window, height=10, width=50)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = tk.Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

# Buttons
tk.Button(window, text="View All", width=12, command=refresh_listbox).grid(row=2, column=3)
tk.Button(window, text="Search", width=12, command=search_books).grid(row=3, column=3)
tk.Button(window, text="Add Book", width=12, command=add_book).grid(row=4, column=3)
tk.Button(window, text="Update Selected", width=12, command=update_book).grid(row=5, column=3)
tk.Button(window, text="Delete Selected", width=12, command=delete_book).grid(row=6, column=3)
tk.Button(window, text="Close", width=12, command=window.destroy).grid(row=7, column=3)

# Initialize listbox with current books
refresh_listbox()

# Start GUI
window.mainloop()