from password_manager.manager import authenticate, add_password, view_passwords, search_password


def main():
    print("=== Password Manager CLI ===")
    authenticate()

    while True:
        print("\n1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
