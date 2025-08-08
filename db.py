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

def get_connection():
    return sqlite3.connect("accounts.db")

def commit_and_close_connection(conn):
    conn.commit()
    conn.close()

def add_account_to_db(website, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO accounts (website, email, password) VALUES (?, ?, ?)",
        (website, email, password)
    )

    commit_and_close_connection(conn)

def search_db_for_accounts(website):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM accounts WHERE website = ?",
        (website, )
    )
    rows = cursor.fetchall()

    commit_and_close_connection(conn)

    accounts = []
    for row in rows:
        accounts.append({
            "id": row[0],
            "website": row[1],
            "email": row[2],
            "password": row[3]
        })
    return accounts

def delete_accounts_from_db(website):
    conn = get_connection()
    cursor = conn.cursor()

    cursor. execute(
        "DELETE FROM accounts WHERE website = ?",
        (website, )
    )

    commit_and_close_connection(conn)
