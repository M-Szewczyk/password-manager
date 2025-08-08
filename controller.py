import db
from db import add_account_to_db, search_db_for_account
from tkinter import messagebox
import random
import string

def add_credentials(website, email, password):
    if not website or not email or not password:
        messagebox.showwarning("Missing information", "Please fill in all fields.")
        return False

    existing_accounts = db.search_db_for_account(website)
    print(existing_accounts)
    for account in existing_accounts:
        if account["email"] == email:
            messagebox.showwarning("Duplicate entry",f"This email is already in use for {website}.")
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

def show_credentials(website):
    accounts = search_db_for_account(website)

    if not accounts:
        messagebox.showinfo("No credentials found", "No credentials were found for this website.")
        return

    message = f"Website: {website} \n"
    for account in accounts:
        message += f"Email: {account["email"]} \nPassword: {account["password"]} \n\n"
    messagebox.showinfo("Credentials found", message.strip())