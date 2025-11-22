numbers = [15, 8, 31, 47, 2, 19]

print("Array values:")
for num in numbers:
    print(num, end=' ')
print()

total = 0
for num in numbers:
    total += num

mean = total / len(numbers)

print("Arithmetic mean:", mean)
