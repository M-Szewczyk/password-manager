from db import initialize_db
from ui import UserInterface
from tkinter import simpledialog, messagebox
from crypto import init_with_master_password


def main():
    master_password = simpledialog.askstring("Master Password", "Enter master password:", show ="*")
    if not master_password:
        messagebox.showerror("Error", "Password cannot be an empty string. Exiting the app.")
        exit()

    if not init_with_master_password(master_password):
        messagebox.showerror("Wrong password", "The master password is incorrect. Exiting the app.")
        exit()

    initialize_db()
    UserInterface()

if __name__ == "__main__":
    main()