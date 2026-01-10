import json

product = {}
product['name'] = input("Product name: ")
product['price'] = float(input("Price: "))
product['paid'] = input("Paid (yes/no): ").lower() == 'yes'

with open('product.json', 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)

print("Product data saved")
