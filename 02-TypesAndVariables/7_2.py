###
# A program that checks whether the password length
# read from the keyboard is correct.
#
password = input('Enter password: ')
password_ok = "YES" if len(password) >= 8 else "NO"
print(f'Password length is valid: {password_ok}')