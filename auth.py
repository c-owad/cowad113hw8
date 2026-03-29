# Phase 3: Fixes after AI review
import json
import os
import hashlib

USERS_FILE = 'users.json'

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
    return hashlib.sha256(password.encode() + salt).hexdigest(), salt

def register(username, password):
    if not username.isalnum() or not password.isalnum():
        raise ValueError("Username and password must be alphanumeric.")
    users = load_users()
    if username in users:
        raise ValueError("Username already exists.")
    hashed, salt = hash_password(password)
    users[username] = {'hash': hashed, 'salt': salt.hex()}
    save_users(users)
    print("Registration successful.")

def login(username, password):
    if not username.isalnum() or not password.isalnum():
        raise ValueError("Username and password must be alphanumeric.")
    users = load_users()
    if username not in users:
        raise ValueError("Invalid username or password.")
    user_data = users[username]
    if isinstance(user_data, str):  # old plain text, for migration
        if user_data == password:
            # migrate to hash
            hashed, salt = hash_password(password)
            users[username] = {'hash': hashed, 'salt': salt.hex()}
            save_users(users)
            print("Login successful.")
        else:
            raise ValueError("Invalid username or password.")
    else:
        stored_hash = user_data['hash']
        salt = bytes.fromhex(user_data['salt'])
        hashed, _ = hash_password(password, salt)
        if hashed != stored_hash:
            raise ValueError("Invalid username or password.")
        print("Login successful.")