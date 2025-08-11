import sys
from tkinter import simpledialog, messagebox
from crypto import init_with_master_password, master_password_is_set

def prompt_master_password(root):

    root.lift()

    # first launch, "master.hash" file does not exist

    if not master_password_is_set():
        master_password = simpledialog.askstring("Create master password", "Please create the master password:", parent=root)

        if not master_password:
            messagebox.showerror("Empty password","Password cannot be empty!", parent=root)
            root.destroy()
            sys.exit(1)
        reentered_master_password = simpledialog.askstring("Re-enter master password", "Please re-enter the master password:", parent=root)

        if master_password != reentered_master_password:
            messagebox.showerror("Passwords do not match","Passwords do not match. Exiting app.", parent=root)
            root.destroy()
            sys.exit(1)

        init_with_master_password(master_password)

    # normal launch, "master.hash" file does exist
    else:
        master_password = simpledialog.askstring("Enter master password", "Please enter the master password.", parent=root)
        if not master_password:
            messagebox.showerror("Empty password", "Password cannot be empty!", parent=root)
            root.destroy()
            sys.exit(1)
        if not init_with_master_password(master_password):
            messagebox.showerror("Wrong password","You entered the wrong password. Exiting app.", parent=root)
            root.destroy()
            sys.exit(1)

