# Password Manager CLI

A simple and secure command-line password manager built using Python.

## Features
- Master password authentication
- Add new credentials
- View saved credentials
- Search credentials by service name
- Encrypted local storage

## Tech Stack
- Python 3
- cryptography library

## Security
- Uses a master password for authentication
- Passwords are encrypted using Fernet (AES-based)
- Encryption key is derived using PBKDF2 with salt
- Master password is never stored

## Project Status
🚧 In progress
