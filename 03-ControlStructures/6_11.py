current_price = 140.00
previous_price = 200.00

price_drop = ((previous_price - current_price) / previous_price) * 100

print(f"Current product price: {current_price}")
print(f"Previous product price: {previous_price}")

if price_drop >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_drop}%")
else:
    print("Price reduction too small.")
    print(f"Product price reduced by {price_drop}%")
