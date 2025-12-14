from password_manager.storage import load_vault, save_vault, get_salt
from password_manager.utils import generate_key, encrypt_data, decrypt_data

MASTER_KEY = None


def authenticate():
    global MASTER_KEY
    master_password = input("Enter master password: ").strip()

    salt = get_salt()
    MASTER_KEY = generate_key(master_password, salt)


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
        print(f"- {service} | {creds['username']} | {decrypted_pwd}")
