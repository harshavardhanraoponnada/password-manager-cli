from password_manager.storage import load_vault, save_vault


def add_password():
    service = input("Service name: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not service or not username or not password:
        print("\nAll fields are required.")
        return

    vault = load_vault()

    vault[service] = {
        "username": username,
        "password": password
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
        print(f"- {service} | {creds['username']} | {creds['password']}")
