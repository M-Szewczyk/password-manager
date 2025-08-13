import sqlite3
from crypto import encrypt_password, decrypt_password


def initialize_db():
    conn = get_connection()
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
    encrypted_password = encrypt_password(password)

    cursor.execute(
        "INSERT INTO accounts (website, email, password) VALUES (?, ?, ?)",
        (website, email, encrypted_password)
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

    conn.close()

    accounts = []
    for row in rows:
        decrypted_password = decrypt_password(row[3])
        accounts.append({
            "id": row[0],
            "website": row[1],
            "email": row[2],
            "password": decrypted_password
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
