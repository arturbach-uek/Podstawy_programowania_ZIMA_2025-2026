prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}
cart = {'juice': 3, 'bread': 1, 'milk': 2}

total = sum(prices[item] * quantity for item, quantity in cart.items())
print("Total cost:", round(total, 2))
