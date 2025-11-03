amount = int(input("Ener the amoint in PLN: "))

coins_5 = amount // 5
amount %= 5

coins_2 = amount // 2
amount %= 2

coins_1 = amount // 1
amount %= 1

print(f"The amount of PLN {amount + coins_2 * 2 + coins_5 * 5} in coins:")
print(f"5 PLN coins: {coins_5}")
print(f"2 PLN coins: {coins_2}")
print(f"1 PLN coins: {coins_1}")