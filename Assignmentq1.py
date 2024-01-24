def check_password_strength(password):
    
    if len(password) < 8:
        return False
    
    
    elif not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False
    
    
    elif not any(char.isdigit() for char in password):
        return False
    
    
    elif not any(char in "!@#$%" for char in password):
        return False
    
    return True


user_password = input("Enter your password: ")


if check_password_strength(user_password):
    print("Password is strong!")
else:
    print("Password does not meet the criteria. Please ensure it has at least 8 characters, both uppercase and lowercase letters, at least one digit, and at least one special character.")
