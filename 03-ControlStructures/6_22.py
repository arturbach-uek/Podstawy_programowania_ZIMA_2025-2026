for number in range(1, 31):
    if number % 3 == 0:
        print("THREE")
    elif number % 5 == 0:
        print("FIVE")
    elif number % 3 == 0 and number % 5 == 0:
        print("BINGO")
    else:
        print(number)