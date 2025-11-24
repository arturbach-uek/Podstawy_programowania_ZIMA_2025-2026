num_products = int(input("Enter the number of products purchased: "))
product_price = float(input("Enter the product price: "))

if num_products <= 2:
    total = num_products * product_price
else:
    total = 2 * product_price
    discounted_products = num_products - 2
    total += discounted_products * product_price * 0.75

print(f"Amount to pay: {total:.2f}")