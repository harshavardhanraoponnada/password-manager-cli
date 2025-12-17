import tkinter as tk
from tkinter import messagebox
from password_manager.manager import authenticate


class PasswordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("400x300")
        self.root.configure(bg="#f4f6f7")

        self.login_screen()

    def login_screen(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg="#f4f6f7")
        frame.pack(expand=True)

        tk.Label(
            frame,
            text="🔐 Password Manager",
            font=("Arial", 16, "bold"),
            bg="#f4f6f7"
        ).pack(pady=10)

        tk.Label(frame, text="Master Password", bg="#f4f6f7").pack()
        self.master_entry = tk.Entry(frame, show="*", width=25)
        self.master_entry.pack(pady=5)

        tk.Button(
            frame,
            text="Unlock Vault",
            width=20,
            bg="#2e86c1",
            fg="white",
            command=self.authenticate_user
        ).pack(pady=15)

    def authenticate_user(self):
        try:
            authenticate(self.master_entry.get())
            self.dashboard()
        except Exception:
            messagebox.showerror("Error", "Incorrect master password")

    def dashboard(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg="#f4f6f7")
        frame.pack(expand=True)

        tk.Label(
            frame,
            text="Dashboard",
            font=("Arial", 14, "bold"),
            bg="#f4f6f7"
        ).pack(pady=10)

        buttons = [
            "Add Password",
            "View Passwords",
            "Search Password",
            "Update Password",
            "Delete Password"
        ]

        for text in buttons:
            tk.Button(
                frame,
                text=text,
                width=25,
                pady=5,
                bg="#5dade2",
                fg="white"
            ).pack(pady=4)

        tk.Button(
            frame,
            text="Exit",
            width=25,
            bg="#a93226",
            fg="white",
            command=self.root.quit
        ).pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


def run_gui():
    root = tk.Tk()
    PasswordManagerGUI(root)
    root.mainloop()
