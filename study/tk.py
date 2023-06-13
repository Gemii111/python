import tkinter as tk
from tkinter import ttk
import pyodbc

# Set up the connection parameters
server = '<DESKTOP-J172NJ7\SQL2019STD>'
database = '<Clinic>'
username = '<>'
password = '<>'

# Create the connection string
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def display_data():
    try:
        # Connect to the database
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Execute a SQL query
        cursor.execute("SELECT * FROM your_table")

        # Fetch all rows
        rows = cursor.fetchall()

        # Clear existing rows in the table
        for item in treeview.get_children():
            treeview.delete(item)

        # Insert fetched data into the table
        for row in rows:
            treeview.insert('', 'end', values=row)

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except pyodbc.Error as e:
        print(f"An error occurred: {e}")

# Create the main window
window = tk.Tk()
window.title("Data Viewer")

# Create the Treeview widget for the table
treeview = ttk.Treeview(window)
treeview.pack(padx=10, pady=10)

# Define table columns
treeview["columns"] = ("column1", "column2", "column3")

# Configure column headings
treeview.heading("column1", text="Column 1")
treeview.heading("column2", text="Column 2")
treeview.heading("column3", text="Column 3")

# Configure column widths
treeview.column("column1", width=100)
treeview.column("column2", width=100)
treeview.column("column3", width=100)

# Add a button to fetch and display data
button_fetch = tk.Button(window, text="Fetch Data", command=display_data)
button_fetch.pack(pady=10)

# Run the main window loop
window.mainloop()
