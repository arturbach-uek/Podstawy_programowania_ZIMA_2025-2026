def sum_of_numbers_in_range(x, y):
    total = 0
    for number in range(x, y + 1):
        if number % 6 == 0 and number % 4 != 0:
            numbers += number
    return total

print(sum_of_numbers_in_range(1, 20))