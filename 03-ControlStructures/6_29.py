N = int(input("Enter how many prime number you want to display: "))
counter = 0
number = 2

print("Prime numbers: ", end=" ")

while counter < N:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")
        counter += 1