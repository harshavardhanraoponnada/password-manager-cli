from password_manager.storage import load_vault, save_vault, get_salt
from password_manager.utils import generate_key, encrypt_data, decrypt_data

MASTER_KEY = None

from cryptography.fernet import InvalidToken

def authenticate():
    global MASTER_KEY
    master_password = input("Enter master password: ").strip()

    salt = get_salt()
    key = generate_key(master_password, salt)

    vault = load_vault()
    if vault:
        try:
            sample = next(iter(vault.values()))
            decrypt_data(sample["password"], key)
        except InvalidToken:
            print("❌ Incorrect master password.")
            exit(1)

    MASTER_KEY = key



def add_password():
    service = input("Service name: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not service or not username or not password:
        print("All fields are required.")
        return

    encrypted_pwd = encrypt_data(password, MASTER_KEY)

    vault = load_vault()
    vault[service] = {
        "username": username,
        "password": encrypted_pwd
    }

    save_vault(vault)
    print(f"Password saved for {service}.")


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
