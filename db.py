import sqlite3


def initialize_db():

    conn = sqlite3.connect("accounts.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL 
        )
        '''
    )

    conn.commit()
    conn.close()

def add_account(website, email, password):

    conn = sqlite3.connect("accounts.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO accounts (website, email, password) VALUES (?, ?, ?)",
        (website, email, password)
    )

    conn.commit()
    conn.close()



