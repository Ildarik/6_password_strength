import getpass
import re

def get_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"\W", password) is None
    
    if length_error:
    	return 1
    elif lowercase_error:
    	return 2
    elif digit_error:
        return 4	
    elif symbol_error:
        return 6
    elif uppercase_error:
    	return 8
    else:
    	return 10


if __name__ == '__main__':
    password = getpass.getpass(prompt="Please type password: ")
    print("Password strength: ", get_password_strength(password))
