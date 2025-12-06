import re as regular_expressions

username = input("Enter username: ")
password = input("Enter password: ")

username_pattern = r'^[a-z]{6,}$'
password_pattern = r'^[A-Za-z0-9_]{8,}$'

if regular_expressions.match(username_pattern, username) and regular_expressions.match(password_pattern, password):
    print("Username and password are valid")
else:
    print("Invalid username or password")
