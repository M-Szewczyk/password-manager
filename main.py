from db import initialize_db
from ui import UserInterface
from tkinter import Tk
from validation import prompt_master_password


def main():
    initialize_db()

    root = Tk()
    UserInterface(root)

    root.after_idle(prompt_master_password, root)
    root.mainloop()

if __name__ == "__main__":
    main()