from tkinter import *
from tkinter import ttk
from controller import add_credentials
import sv_ttk

class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)

        # applying theme
        sv_ttk.set_theme("dark")


        # lock logo
        self.canvas = Canvas(width=300, height=300)
        self.lock_img = PhotoImage(file="lock_art300x300.png")
        self.canvas.create_image(150, 150, image=self.lock_img)
        self.canvas.grid(row=0,column=1)

        # labels
        self.website_label = ttk.Label(text="Website:", font=("Arial",28, "normal"))
        self.website_label.grid(row=1, column=0, padx=10)

        self.email_label = ttk.Label(text="Email/Username:", font=("Arial",28, "normal"))
        self.email_label.grid(row=2, column=0, padx=10)

        self.password_label = ttk.Label(text="Password:", font=("Arial",28, "normal"))
        self.password_label.grid(row=3, column=0, padx=10)

        # entries
        self.website_entry = ttk.Entry(width=21, font=("Arial",28, "normal"))
        self.website_entry.grid(row=1, column=1, sticky="ew", padx=2, pady=2)
        self.website_entry.focus()

        self.email_entry = ttk.Entry(font=("Arial",28, "normal"))
        self.email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

        self.password_entry = ttk.Entry(width=21, font=("Arial",28,"normal"))
        self.password_entry.grid(row=3, column=1, sticky="ew", padx=2, pady=2)

        self.generate_password_button = Button(text="Generate Password", font=("Arial",20, "normal"))
        self.generate_password_button.grid(row=3, column=2, sticky="ew", padx=10, pady=10)

        self.add_button = Button(text="Add", font=("Arial",20, "normal"), command=self.add_button_on_clicked)
        self.add_button.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=10)

        self.search_button = Button(text="Search", font=("Arial",20, "normal"))
        self.search_button.grid(row=1, column=2, sticky="ew", padx=10, pady=10)

        self.window.mainloop()

    def clear_input_fields(self):
        self.website_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def get_input_fields(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        return website, email, password

    def add_button_on_clicked(self):
        website, email, password = self.get_input_fields()

        success = add_credentials(website, email, password)

        if success:
            self.clear_input_fields()

