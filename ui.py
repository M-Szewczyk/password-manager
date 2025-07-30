from tkinter import *
from tkinter import messagebox, ttk
import sv_ttk

class UserInterface:
    def __init__(self):
        window = Tk()
        window.title("Password Manager")
        window.config(padx=50, pady=50)

        # applying theme
        sv_ttk.set_theme("dark")


        # lock logo
        canvas = Canvas(width=300, height=300)
        lock_img = PhotoImage(file="lock_art300x300.png")
        canvas.create_image(150, 150, image=lock_img)
        canvas.grid(row=0,column=1)

        # labels
        website_label = ttk.Label(text="Website:", font=("Arial",28, "normal"))
        website_label.grid(row=1, column=0, padx=10)
        email_label = ttk.Label(text="Email/Username:", font=("Arial",28, "normal"))
        email_label.grid(row=2, column=0, padx=10)
        password_label = ttk.Label(text="Password:", font=("Arial",28, "normal"))
        password_label.grid(row=3, column=0, padx=10)

        # entries
        website_entry = ttk.Entry(width=21, font=("Arial",28, "normal"))
        website_entry.grid(row=1, column=1, sticky="ew", padx=2, pady=2)
        website_entry.focus()
        email_entry = ttk.Entry(font=("Arial",28, "normal"))
        email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
        password_entry = ttk.Entry(width=21, font=("Arial",28,"normal"))
        password_entry.grid(row=3, column=1, sticky="ew", padx=2, pady=2)

        generate_password_button = Button(text="Generate Password", font=("Arial",20, "normal"))
        generate_password_button.grid(row=3, column=2, sticky="ew", padx=10, pady=10)
        add_button = Button(text="Add", font=("Arial",20, "normal"))
        add_button.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=10)
        search_button = Button(text="Search", font=("Arial",20, "normal"))
        search_button.grid(row=1, column=2, sticky="ew", padx=10, pady=10)

        window.mainloop()