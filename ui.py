from tkinter import *
from tkinter import ttk
from controller import add_credentials, generate_password, show_credentials, delete_credentials
import sv_ttk





class UserInterface:
    def __init__(self, root):
        self.window = setup_window(root)

        set_theme("dark")

        add_logo(root)

        add_labels(root)

        self.website_entry, self.email_entry, self.password_entry = add_entries(root)

        self.generate_password_button, self.add_button, self.search_button, self.delete_button = add_buttons(self,root)


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

    def generate_password_button_on_clicked(self):
        random_password = generate_password()
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, random_password)

    def search_button_on_clicked(self):
        website = self.website_entry.get()
        show_credentials(website)

    def delete_button_on_clicked(self):
        website = self.website_entry.get()
        delete_credentials(website)
        self.clear_input_fields()


def setup_window(root):
    window = root
    window.title("Password Manager")
    window.config(padx=50, pady=50)
    return window

def set_theme(theme_name):
    sv_ttk.set_theme(theme_name)

def add_logo(root):
    root.canvas = Canvas(width=300, height=300)
    root.lock_img = PhotoImage(file="lock_art300x300.png")
    root.canvas.create_image(150, 150, image=root.lock_img)
    root.canvas.grid(row=0, column=1)

def add_labels(root):
    root.website_label = ttk.Label(text="Website:", font=("Arial", 28, "normal"))
    root.website_label.grid(row=1, column=0, padx=10)

    root.email_label = ttk.Label(text="Email/Username:", font=("Arial", 28, "normal"))
    root.email_label.grid(row=2, column=0, padx=10)

    root.password_label = ttk.Label(text="Password:", font=("Arial", 28, "normal"))
    root.password_label.grid(row=3, column=0, padx=10)


def add_entries(root):
    root.website_entry = ttk.Entry(width=21, font=("Arial", 28, "normal"))
    root.website_entry.grid(row=1, column=1, sticky="ew", padx=2, pady=2)
    root.website_entry.focus()

    root.email_entry = ttk.Entry(font=("Arial", 28, "normal"))
    root.email_entry.grid(row=2, column=1, columnspan=3, sticky="ew")

    root.password_entry = ttk.Entry(width=21, font=("Arial", 28, "normal"))
    root.password_entry.grid(row=3, column=1, sticky="ew", padx=2, pady=2)

    return root.website_entry, root.email_entry, root.password_entry

def add_buttons(ui,root):
    root.generate_password_button = Button(text="Generate Password", font=("Arial", 20, "normal"),
                                           command=ui.generate_password_button_on_clicked)
    root.generate_password_button.grid(row=3, column=2, columnspan=2, sticky="ew", padx=10, pady=10)

    root.add_button = Button(text="Add", font=("Arial", 20, "normal"), command=ui.add_button_on_clicked)
    root.add_button.grid(row=4, column=1, columnspan=3, sticky="ew", padx=10, pady=10)

    root.search_button = Button(text="Search", font=("Arial", 20, "normal"), command=ui.search_button_on_clicked)
    root.search_button.grid(row=1, column=2, sticky="ew", padx=10, pady=10)

    root.delete_button = Button(text="Delete", font=("Arial", 20, "normal"), command=ui.delete_button_on_clicked)
    root.delete_button.grid(row=1, column=3, sticky="ew", padx=10, pady=10)

    return root.generate_password_button, root.add_button, root.search_button, root.delete_button