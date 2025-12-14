import json
import os

VAULT_PATH = "data/vault.json"
SALT_PATH = "data/salt.bin"


def get_salt():
    if not os.path.exists(SALT_PATH):
        salt = os.urandom(16)
        with open(SALT_PATH, "wb") as f:
            f.write(salt)
        return salt

    with open(SALT_PATH, "rb") as f:
        return f.read()


def load_vault():
    if not os.path.exists(VAULT_PATH):
        return {}

    with open(VAULT_PATH, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_vault(data):
    with open(VAULT_PATH, "w") as file:
        json.dump(data, file, indent=4)
