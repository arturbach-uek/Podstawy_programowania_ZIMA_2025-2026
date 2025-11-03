hours = int(input("Enter the number of parking hours: "))

if 1 <= hours <= 2:
    fee = 5
elif 3 <= hours <= 6:
    fee = 15
elif hours > 6:
    fee = 20
else:
    fee = 0

print("Parking fee:", fee, "PLN")