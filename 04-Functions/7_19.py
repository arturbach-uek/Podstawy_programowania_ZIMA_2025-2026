def sum_of_repeated_digits(number):
    number_str = str(number)
    result = 0
    counted = []
    
    for digit in number_str:
        if number_str.count(digit) > 1 and digit not in counted:
            result += int(digit)
            counted.append(digit)
                
    return result


print(sum_of_repeated_digits(1027))
