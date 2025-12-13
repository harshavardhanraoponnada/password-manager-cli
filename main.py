from password_manager.manager import add_password, view_passwords


def main():
    while True:
        print("\n=== Password Manager CLI ===")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
