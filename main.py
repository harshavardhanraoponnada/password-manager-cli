from password_manager.manager import authenticate, add_password, view_passwords, search_password, update_password, delete_password


def main():
    print("=== Password Manager CLI ===")
    authenticate()

    while True:
        print("\n1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Update Password")
        print("5. Delete Password")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
            break
        elif choice == "4":
            update_password()
        elif choice == "5":
            delete_password()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
