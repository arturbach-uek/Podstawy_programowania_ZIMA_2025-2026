decimal_number = int(input("Enter decimal number: "))
oryginal_number = decimal_number
binary = ""
if decimal_number == 0:
    binary = "0"
else:
    while decimal_number > 0:
        binary = str(decimal_number % 2) + binary
        decimal_number = decimal_number // 2

print(f"{oryginal_number}(10) = {binary}(2)")