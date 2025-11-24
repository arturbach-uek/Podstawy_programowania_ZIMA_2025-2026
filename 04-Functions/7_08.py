def min_to_pay(amount_to_pay):
    coins = [5, 2, 1]
    count = 0
    remaining = amount_to_pay

    for coin in coins:
        count += remaining // coin
        remaining = remaining % coin

    return count

print(min_to_pay(23))