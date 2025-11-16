def count_negative_even(x, y):
    return sum(1 for number in range(x, y) if number < 0 and number % 2 == 0)

print(count_negative_even(-7, 8))