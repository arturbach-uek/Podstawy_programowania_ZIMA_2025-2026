def is_valid_binary(number):
    return all(digit in ["0", "1"] for digit in number)

print(is_valid_binary("101101"))
print(is_valid_binary("1311a10100"))