import json
import os

USERS_FILE = 'users.json'

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

def register(username, password):
    if not username.isalnum() or not password.isalnum():
        raise ValueError("Username and password must be alphanumeric.")
    users = load_users()
    if username in users:
        raise ValueError("Username already exists.")
    users[username] = password
    save_users(users)
    print("Registration successful.")

def login(username, password):
    if not username.isalnum() or not password.isalnum():
        raise ValueError("Username and password must be alphanumeric.")
    users = load_users()
    if username not in users or users[username] != password:
        raise ValueError("Invalid username or password.")
    print("Login successful.")