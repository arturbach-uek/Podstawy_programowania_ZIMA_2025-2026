price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

total_before = sum(price_list.values())
print("Before discount:")
for key, value in price_list.items():
    print(key, value)

print("Total:", total_before)

for key in price_list:
    price_list[key] = round(price_list[key] * 0.9, 2)

total_after = sum(price_list.values())
print("After discount:")
for key, value in price_list.items():
    print(key, value)

print("Total:", total_after)
