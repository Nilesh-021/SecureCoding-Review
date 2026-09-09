# secure_app.py
# CodeAlpha - Secure Coding Review
# Educational demonstration only

import sqlite3
import hashlib
import secrets

DATABASE = "secure_users.db"


def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def hash_password(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100_000
    ).hex()


def register_user(username, password):
    # Input validation
    username = username.strip()

    if not username or len(username) > 50:
        print("Invalid username.")
        return

    if len(password) < 8:
        print("Password must contain at least 8 characters.")
        return

    salt = secrets.token_bytes(16)
    password_hash = hash_password(password, salt)

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Parameterized query prevents SQL injection
    query = """
        INSERT INTO users (username, password_hash, salt)
        VALUES (?, ?, ?)
    """

    try:
        cursor.execute(
            query,
            (username, password_hash, salt.hex())
        )
        connection.commit()
        print("User registered successfully.")

    except sqlite3.IntegrityError:
        print("Username already exists.")

    finally:
        connection.close()


def find_user(username):
    username = username.strip()

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Parameterized query
    query = "SELECT username FROM users WHERE username = ?"

    cursor.execute(query, (username,))
    result = cursor.fetchone()

    connection.close()

    return result


def main():
    create_database()

    print("Secure Coding Review - Secure Application")

    username = input("Enter username: ")
    password = input("Enter password: ")

    register_user(username, password)

    user = find_user(username)

    if user:
        print("User found.")
    else:
        print("User not found.")


if __name__ == "__main__":
    main()