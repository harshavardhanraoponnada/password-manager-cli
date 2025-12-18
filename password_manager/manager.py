from password_manager.storage import load_vault, save_vault, get_salt
from password_manager.utils import generate_key, encrypt_data, decrypt_data, check_password_strength

MASTER_KEY = None

from cryptography.fernet import InvalidToken

def authenticate(master_password):
    global MASTER_KEY

    salt = get_salt()
    key = generate_key(master_password, salt)

    vault = load_vault()
    if vault:
        try:
            sample = next(iter(vault.values()))
            decrypt_data(sample["password"], key)
        except InvalidToken:
            raise ValueError("Invalid master password")

    MASTER_KEY = key
    return True


def add_password():
    service = input("Service name: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not service or not username or not password:
        print("All fields are required.")
        return
    
    strength = check_password_strength(password)
    print(f"\nPassword strength: {strength}")

    encrypted_pwd = encrypt_data(password, MASTER_KEY)

    vault = load_vault()
    vault[service] = {
        "username": username,
        "password": encrypted_pwd
    }

    save_vault(vault)
    print(f"\nPassword saved for {service}.")


def view_passwords():
    vault = load_vault()

    if not vault:
        print("No passwords stored.")
        return

    print("\nStored credentials:")
    for service, creds in vault.items():
        decrypted_pwd = decrypt_data(creds["password"], MASTER_KEY)
        masked = "*" * len(decrypted_pwd)
        print(f"- {service} | {creds['username']} | {masked}")

def search_password():
    service = input("Enter service name to search: ").strip()
    vault = load_vault()

    if service not in vault:
        print("Service not found.")
        return

    creds = vault[service]
    decrypted_pwd = decrypt_data(creds["password"], MASTER_KEY)
    masked = "*" * len(decrypted_pwd)
    print(f"{service} | {creds['username']} | {masked}")

def update_password():
    service = input("Enter service name to update: ").strip()
    vault = load_vault()

    if service not in vault:
        print("Service not found.")
        return

    new_password = input("Enter new password: ").strip()

    strength = check_password_strength(new_password)
    print(f"Password strength: {strength}")

    encrypted_pwd = encrypt_data(new_password, MASTER_KEY)

    vault[service]["password"] = encrypted_pwd
    save_vault(vault)

    print(f"Password updated for {service}.")

def delete_password():
    service = input("Enter service name to delete: ").strip()
    vault = load_vault()

    if service not in vault:
        print("Service not found.")
        return

    del vault[service]
    save_vault(vault)

    print(f"Password deleted for {service}.")

import csv

def export_to_csv():
    vault = load_vault()

    if not vault:
        print("No data to export.")
        return

    with open("passwords_export.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Service", "Username"])

        for service, creds in vault.items():
            writer.writerow([service, creds["username"]])

    print("Passwords exported (without passwords).")

def add_password_gui(service, username, password):
    if not service or not username or not password:
        raise ValueError("All fields are required")

    encrypted_pwd = encrypt_data(password, MASTER_KEY)
    vault = load_vault()

    vault[service] = {
        "username": username,
        "password": encrypted_pwd
    }

    save_vault(vault)


def get_all_passwords_gui():
    vault = load_vault()
    result = []

    for service, creds in vault.items():
        decrypted_pwd = decrypt_data(creds["password"], MASTER_KEY)
        masked = "*" * len(decrypted_pwd)
        result.append((service, creds["username"], masked))

    return result
