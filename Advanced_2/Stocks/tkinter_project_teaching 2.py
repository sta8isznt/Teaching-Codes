# Import statements
import tkinter as tk
from tkinter import messagebox
import sqlite3
# Functionalities
def init_db():
    filename = "Stocks.db"
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks(
            symbol TEXT PRIMARY KEY,
            quantity INTEGER,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

def buyStock():
    symbol = symbol_entry.get().strip().upper()
    quantity =  quantity_entry.get().strip()
    price = price_entry.get().strip()

    if not symbol or not quantity.isdigit() or not price.replace('.', '', 1).isdigit():
        messagebox.showerror("Input Error", "Please provide valid input.")
        return
    
    quantity = int(quantity)
    price = float(price)

    conn = sqlite3.connect("Stocks.db")
    cursor = conn.cursor()

    #Check if the stock exists in the table
    cursor.execute('SELECT quantity, price FROM stocks WHERE symbol = ?', (symbol,))
    existing_stock = cursor.fetchone() #(quantity, price)

    if existing_stock:
        existing_quantity, existing_price = existing_stock #(quantity, price)
        total_quantity = existing_quantity + quantity
        new_price = ((existing_quantity * existing_price) + (quantity * price)) / total_quantity

        cursor.execute('UPDATE stocks SET quantity = ?, price = ? WHERE symbol = ?', (total_quantity, new_price, symbol))
        result_label.config(text=f'Updated {symbol} with new quantity {total_quantity} and new price {new_price:.2f}')
    else:
        cursor.execute('INSERT INTO stocks (symbol, quantity, price) VALUES (?,?,?)', 
                       (symbol, quantity, price))
        result_label.config(text=f'Added {symbol} with {quantity} shares at {price:.2f}')

    conn.commit()
    conn.close()

    symbol_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

def sellStock():
    symbol = symbol_entry.get().strip().upper()

    if not symbol:
        messagebox.showerror("Input Error", "Please give a valid symbol!")
        return
    
    conn = sqlite3.connect("Stocks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stocks WHERE symbol=?", (symbol,))
    conn.commit()

    if cursor.rowcount == 0:
        result_label.config(text=f"{symbol} not found in the database!")
    else:
        result_label.config(text=f"{symbol} successfully sold!")

    conn.close()
    symbol_entry.delete(0, tk.END)

def showAllStocks():
    conn = sqlite3.connect("Stocks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT symbol, quantity, price FROM stocks")
    all_stocks = cursor.fetchall()

    if not all_stocks:
        result_label.config(text="Database has no stocks!")
        return
    
    final_list = []
    for stock in all_stocks:
        final_list.append(f"{stock[0]}: {stock[1]} shares at {stock[2]:.2f}€ each")

    result_label.config(text='\n'.join(final_list))

    conn.commit()
    conn.close()

def removeAllStocks():
    conn = sqlite3.connect("Stocks.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stocks")
    conn.commit()
    conn.close()
    result_label.config(text="All stocks have been deleted successfully")

init_db()

# Graphical User Interface - GUI
# Main Window
root = tk.Tk()

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

result_label = tk.Label(root, text="Result will appear here", wraplength=300)
result_label.grid(row=5, column=0, columnspan= 2, padx=5, pady=5)

# Entries
symbol_entry = tk.Entry(root)
symbol_entry.grid(row=0, column=1, padx=10, pady=10)

quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1, padx=10, pady=10)

# Buttons
buyStock_button = tk.Button(root, text="Buy Stock", command=buyStock)
buyStock_button.grid(row=3, column=0, padx=10, pady=10)

sellStock_button = tk.Button(root, text="Sell Stock", command=sellStock)
sellStock_button.grid(row=4, column=0, padx=10, pady=10)

showAllStocks_button = tk.Button(root, text="Show Stock", command=showAllStocks)
showAllStocks_button.grid(row=3, column=1, padx=10, pady=10)

removeAllStocks_button = tk.Button(root, text="Remove all Stocks", command=removeAllStocks)
removeAllStocks_button.grid(row=4, column=1, padx=10, pady=10)

# mainLoop
root.mainloop()