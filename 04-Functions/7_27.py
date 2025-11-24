def is_valid_product_code(product_code):
    reminder = sum(int(digit) for digit in product_code[:3]) % 7
    control_digit = int(product_code[-1])
    return reminder == control_digit

print(_("1082"))