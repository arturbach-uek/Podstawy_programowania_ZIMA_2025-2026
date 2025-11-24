price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
reduction = price * (discount / 100)
price_with_discount = price - reduction
print(f"Price with discount: {round(price_with_discount, 2)}")
print(f"Reduction: {round(reduction, 2)}")
