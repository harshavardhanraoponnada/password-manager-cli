import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet


def generate_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(
        kdf.derive(master_password.encode())
    )


def encrypt_data(data: str, key: bytes) -> str:
    fernet = Fernet(key)
    return fernet.encrypt(data.encode()).decode()


def decrypt_data(token: str, key: bytes) -> str:
    fernet = Fernet(key)
    return fernet.decrypt(token.encode()).decode()
