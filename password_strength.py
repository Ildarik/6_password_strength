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

    if (digit_error and (uppercase_error or lowercase_error) and symbol_error):
    	return 2
    
    # if any 2 errors = False
    if (digit_error + uppercase_error + lowercase_error + symbol_error == 2):
    	return 5
    
    # if any 3 errors = False
    if (digit_error + uppercase_error + lowercase_error + symbol_error == 1):
        return 8	

    if not(digit_error or uppercase_error or lowercase_error or symbol_error):
    	return 10


if __name__ == '__main__':
    password = getpass.getpass(prompt="Please type password: ")
    print("Password strength: ", get_password_strength(password))