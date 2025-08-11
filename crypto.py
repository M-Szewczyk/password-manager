import os, base64, hashlib
from typing import Optional
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

SALT_FILE = "salt.bin"
MASTER_HASH_FILE = "master.hash"
_fernet: Optional[Fernet] = None

def _ensure_salt():
    if not os.path.exists(SALT_FILE):
        with open(SALT_FILE, "wb") as f:
            f.write(os.urandom(16))

def _load_salt():
    with open(SALT_FILE, "rb") as f:
        return f.read()

def _get_key(master_password):
    salt = _load_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600000
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

def _save_master_hash(key):
    with open(MASTER_HASH_FILE, "wb") as f:
        f.write(hashlib.sha256(key).digest())

def _load_master_hash():
    with open(MASTER_HASH_FILE, "rb") as f:
        return f.read()

def master_password_is_set():
    return os.path.exists(MASTER_HASH_FILE)


def init_with_master_password(master_password):
    global _fernet
    _ensure_salt()
    key = _get_key(master_password)
    if not master_password_is_set():
        _save_master_hash(key)
    else:
        if hashlib.sha256(key).digest() != _load_master_hash():
            return False
    _fernet = Fernet(key)
    return True

def encrypt_password(password):
    if _fernet is None:
        raise RuntimeError("Encryption not initialized")
    return _fernet.encrypt(password.encode()).decode()

def decrypt_password(token):
    if _fernet is None:
        raise RuntimeError("Encryption not initialized")
    return _fernet.decrypt(token.encode()).decode()