import tkinter as tk
import sqlite3
filename = 'Stocks.db'

def init_db():
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    sqlite_statement = '''
        CREATE TABLE IF NOT EXISTS stocks(
            name TEXT PRIMARY KEY,
            quantity INTEGER,
            price REAL
        )
    '''
    cursor.execute(sqlite_statement)
    conn.commit()
    conn.close()

def add_stock():
    name = item_name_entry.get().strip().upper()
    quantity = item_qty_entry.get().strip()
    price = item_price_entry.get().strip()

    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    sqlite_statement = 'SELECT quantity, price FROM stocks WHERE name = ?'
    cursor.execute(sqlite_statement, (name,))
    conn.commit()
    conn.close()

root = tk.Tk()
root.title("stocks")

init_db()

#Creating Labels and Entry Boxes
item_name_label = tk.Label(root, text="Stock Ticker:")
item_name_label.grid(row=0, column=0, padx=5, pady=5)
item_name_entry = tk.Entry(root)
item_name_entry.grid(row=0, column=1, padx=5, pady=5)

item_qty_label = tk.Label(root, text="Quantity:")
item_qty_label.grid(row=1, column=0, padx=5, pady=5)
item_qty_entry = tk.Entry(root)
item_qty_entry.grid(row=1, column=1, padx=5, pady=5)

item_price_label = tk.Label(root, text="Price:")
item_price_label.grid(row=2, column=0, padx=5, pady=5)
item_price_entry = tk.Entry(root)
item_price_entry.grid(row=2, column=1, padx=5, pady=5)

#Creating Buttons
add_button = tk.Button(root, text="Add Stock", command=add_stock)
add_button.grid(row=3, column=0, padx=5, pady=5)
root.mainloop()