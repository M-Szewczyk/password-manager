from db import add_account_to_db
from tkinter import messagebox
import random
import string

def add_credentials(website, email, password):
    if not website or not email or not password:
        messagebox.showwarning("Missing information", "Please fill in all fields.")
        return False

    try:
        add_account_to_db(website, email, password)
        messagebox.showinfo("Account added","The account was successfully added to the database.")
        return True

    except Exception as e:
        messagebox.showerror("Error",f"Error while saving account: {e}")
        return False

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choice(characters) for i in range(16))
    return random_password

