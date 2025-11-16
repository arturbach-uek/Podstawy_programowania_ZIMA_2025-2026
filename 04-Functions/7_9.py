def sum_of_digits(number, even):
    if even:
        return sum(int(digit) for digit in str(number) if int(digit) % 2 == 0)
    return sum(int(digit) for digit in str(number) if int(digit) % 2 != 0)

print(sum_of_digits(20576, False))