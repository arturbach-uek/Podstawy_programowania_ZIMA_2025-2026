def calculate(expression):
    total = 0
    current_number = ""
    current_operator = "+"

    for char in expression:
        if char.isdigit():
            current_number += char
        else:
            number = int(current_number)

            if current_operator == "+":
                total += number
            else:
                total -= number
            
            current_number = ""
            current_operator = char

    number = int(current_number)
    if current_operator == "+":
        total += number
    else:
        total -= number
    
    return total