arr = [4.5, 7.2, 3.1, 8.0, 10.5, 1.2, 6.8]

value = float(input("Enter a number to check: "))
count = count = sum(1 for num in arr if num > value)

print("Number of elements greater than", value, ":", count)

