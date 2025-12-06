def add_product(product):
    with open('shopping_list.txt', 'a') as f:
        f.write(product + '\n')

product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product != "0":
        add_product(product)