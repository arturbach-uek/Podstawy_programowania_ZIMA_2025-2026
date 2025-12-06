with open("car_park.txt", "r") as file:
    cars = [line.strip() for line in file]
    total = sum(int(number) for number in cars)
    print(total)