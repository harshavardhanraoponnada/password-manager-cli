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

def check_password_strength(password: str) -> str:
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()" for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    else:
        return "Strong"
