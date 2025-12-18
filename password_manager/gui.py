import tkinter as tk
from tkinter import messagebox
from password_manager.manager import authenticate
from password_manager.manager import add_password_gui, get_all_passwords_gui

class PasswordManagerGUI:
    def add_password_form(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg="#f4f6f7")
        frame.pack(expand=True)

        tk.Label(frame, text="Add Password", font=("Arial", 14, "bold"),
                bg="#f4f6f7").pack(pady=10)

        tk.Label(frame, text="Service", bg="#f4f6f7").pack()
        service_entry = tk.Entry(frame, width=30)
        service_entry.pack(pady=3)

        tk.Label(frame, text="Username", bg="#f4f6f7").pack()
        username_entry = tk.Entry(frame, width=30)
        username_entry.pack(pady=3)

        tk.Label(frame, text="Password", bg="#f4f6f7").pack()
        password_entry = tk.Entry(frame, show="*", width=30)
        password_entry.pack(pady=3)

        def save():
            try:
                add_password_gui(
                    service_entry.get(),
                    username_entry.get(),
                    password_entry.get()
                )
                messagebox.showinfo("Success", "Password saved successfully")
                self.dashboard()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(frame, text="Save", bg="#2ecc71",
                fg="white", width=20, command=save).pack(pady=10)

        tk.Button(frame, text="Back", width=20,
                command=self.dashboard).pack()

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
        except Exception:
            messagebox.showerror("Error", "Incorrect master password")
            return   # ⛔ STOP here

        self.dashboard()  # ✅ only if authentication succeeds



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


        tk.Button(frame, text="Add Password", width=25, pady=5,
          bg="#5dade2", fg="white",
          command=self.add_password_form).pack(pady=4)

        tk.Button(frame, text="View Passwords", width=25, pady=5,
          bg="#5dade2", fg="white",
          command=self.view_passwords_popup).pack(pady=4)


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
    
    def view_passwords_popup(self):
        data = get_all_passwords_gui()

        if not data:
            messagebox.showinfo("Info", "No passwords stored")
            return

        popup = tk.Toplevel(self.root)
        popup.title("Stored Passwords")
        popup.geometry("400x300")

        for i, header in enumerate(["Service", "Username", "Password"]):
            tk.Label(popup, text=header, font=("Arial", 10, "bold"),
                    borderwidth=1, relief="solid", width=15).grid(row=0, column=i)

        for row, (service, username, masked_pwd) in enumerate(data, start=1):
            tk.Label(popup, text=service, borderwidth=1,
                    relief="solid", width=15).grid(row=row, column=0)
            tk.Label(popup, text=username, borderwidth=1,
                    relief="solid", width=15).grid(row=row, column=1)
            tk.Label(popup, text=masked_pwd, borderwidth=1,
                    relief="solid", width=15).grid(row=row, column=2)


def run_gui():
    root = tk.Tk()
    PasswordManagerGUI(root)
    root.mainloop()
