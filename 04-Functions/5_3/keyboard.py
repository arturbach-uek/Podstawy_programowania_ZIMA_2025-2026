def input_string(message):
    value = input(message)
    return value

def input_integer(message):
    value = input(message)
    return int(value)

def input_real(message):
    value = input(message)
    return float(value)

def input_boolean(message):
    value = input(message).strip().lower()
    if value in ['true', 't', 'yes', 'y', '1']:
        return True
        
    elif value in ['false', 'f', 'no', 'n', '0']:
        return False
    else:
        raise ValueError("Invalid boolean input")
