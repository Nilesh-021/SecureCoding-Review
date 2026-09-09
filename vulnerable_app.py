# vulnerable_app.py
# CodeAlpha - Secure Coding Review
# Educational demonstration only

import sqlite3
import hashlib

DATABASE = "users.db"

def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password TEXT
        )
    """)

    connection.commit()
    connection.close()


def register_user(username, password):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # VULNERABILITY 1:
    # Password is stored using weak MD5 hashing.
    password_hash = hashlib.md5(password.encode()).hexdigest()

    # VULNERABILITY 2:
    # User input is directly inserted into an SQL query.
    query = (
        f"INSERT INTO users (username, password) "
        f"VALUES ('{username}', '{password_hash}')"
    )

    cursor.execute(query)
    connection.commit()
    connection.close()


def find_user(username):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # VULNERABILITY 3:
    # User input is directly placed into the SQL query.
    query = f"SELECT username FROM users WHERE username = '{username}'"

    cursor.execute(query)
    result = cursor.fetchone()

    connection.close()
    return result


def main():
    create_database()

    print("Secure Coding Review - Demo Application")
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