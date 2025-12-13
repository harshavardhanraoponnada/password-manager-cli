import json
import os

VAULT_PATH = "data/vault.json"


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
