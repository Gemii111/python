import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password are correct
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login Successful!")
        open_main_page()
    else:
        messagebox.showerror("Login", "Invalid username or password.")

def open_main_page():
    # Close the login window
    window.destroy()

    # Create the main page window
    main_window = tk.Tk()
    main_window.title("Main Page")

    # Add content to the main page
    label_main = tk.Label(main_window, text="Welcome to the Main Page!", font=title_font)
    label_main.pack(pady=10)

    # Run the main page window loop
    main_window.mainloop()

# Create the login window
window = tk.Tk()
window.title("Login Page")
window.geometry("300x200")

# Set custom fonts
title_font = Font(family="Helvetica", size=16, weight="bold")
label_font = Font(family="Helvetica", size=12)
button_font = Font(family="Helvetica", size=12, weight="bold")

# Create the title label
label_title = tk.Label(window, text="Login Page", font=title_font)
label_title.pack(pady=10)

# Create the username label and entry
label_username = tk.Label(window, text="Username:", font=label_font)
label_username.pack()
entry_username = tk.Entry(window, font=label_font)
entry_username.pack()

# Create the password label and entry
label_password = tk.Label(window, text="Password:", font=label_font)
label_password.pack()
entry_password = tk.Entry(window, show="*", font=label_font)  # Mask the password input
entry_password.pack()

# Create the login button
button_login = tk.Button(window, text="Login", font=button_font, command=validate_login)
button_login.pack(pady=10)

# Run the login window loop
window.mainloop()
