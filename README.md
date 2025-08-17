This is a local password manager that lets you add, store and retrieve credentials for websites. It is built with Python using the Tkinter package for the UI.
I am using a local SQLite database to store information. For a project of that size a simple JSON file would probably do just as well, however, I am using SQL for learning purposes. 
The information provided gets symmetrically encrypted with Fernet module from Cryptography package before it hits the database. 

I have added authorization, so when you first launch the app, you will be asked to create the master password. Make sure you remember it, as it is not stored anywhere. "master.hash" file gets created
after the first use, and it contains a hashed key derived from the password typed in on the first launch. The validation ensures that when you type in the password on every launch besides the first, 
a key is derived from it, then it is hashed and the program checks if the bytes are the same as in the "master.hash" file. To make the encryption more secure, a random salt (16 bytes) is used in the derivation.
Only passwords are encrypted, the website names and emails are stored in plaintext.

The way the flow looks like:

1. You launch the app.
2. You get prompted to create/provide the master password.
3. If the authorization is not successful, the app will close.
   Otherwise, a key is derived from the master password using the PBKDF2-HMAC-SHA256 function. A Fernet instance is created
   with the derived key and it is called for every encrypton/decryption in the program. After that you can use every feature
   of the app.

Features:
1. Adding credentials (Website name, email/username, password) to the database with the 'add' button. (You can have more than one account for a specific website)
2. Searching the database for accounts (You have to provide the website name and click 'search').
3. Deleting accounts from the database (You have to provide the website name and click 'delete').
4. Generating a random 16-characters long password with the 'generate password' button.

Project structure:

- main.py           # used to build UI, initialize the database and prompt authorization
- ui.py             # creates the window, labels, entries, buttons and handles on_click events
- controller.py     # a module used for logic such as the button handlers and input validation. It takes the information from the UI (entries) to the database or from the database to the UI (messageboxes)
- db.py             # used for CRUD operations on the database
- crypto.py         # handles encryption, master-password flow and Fernet singleton
- validation.py     # a simple prompt to validate the master password
- accounts.db       # database in which website names, emails and encrypted passwords are stored
- salt.bin          # random salt for the encryption function
- master.hash       # hashed key derived from the master password

In order to run the project, you need to have the "cryptography" and "sv_ttk" packages installed. 
