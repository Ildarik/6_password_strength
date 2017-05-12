import getpass
import re

def get_password_strength(password):
    result = 1

    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"\W", password) is None

    if not length_error:
        result += 1
    if not digit_error:
        result += 2
    if not uppercase_error:
        result += 2
    if not lowercase_error:
        result += 2
    if not symbol_error:
        result += 2
    
    return result


if __name__ == '__main__':
    password = getpass.getpass(prompt="Please type password: ")
    print("Password strength: ", get_password_strength(password))
