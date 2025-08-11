import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64

SALT_FILE = "salt.bin"

def generate_salt():
    if not os.path.exists(SALT_FILE):
        with open(SALT_FILE, "wb") as f:
            f.write(os.urandom(16))

def load_salt():
    with open(SALT_FILE, "rb") as f:
        return f.read()

def get_key(master_password):
    salt = load_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600000
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

class PasswordEncryptor:
    def __init__(self, master_password):
        self.key = get_key(master_password)
        self.fernet = Fernet(self.key)

    def encrypt(self, password):
        return self.fernet.encrypt(password.encode()).decode()

    def decrypt(self, token):
        return self.fernet.decrypt(token.encode()).decode()