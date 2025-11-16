def check_password(password):

    if len(password) < 6:
        return False
    
    count = []
    for char in password:
        if char not in count:
            return False
        count.append(char)
        
    return True