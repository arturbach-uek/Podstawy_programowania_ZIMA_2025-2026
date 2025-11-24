def concat_numbers(n):
    return "".join(str(number) for number in range(1, n+1))

print(concat_numbers(11))