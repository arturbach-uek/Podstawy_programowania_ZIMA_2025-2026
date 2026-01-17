numbers = [number for number in range(1, 21)]
filtered_numbers = list(filter(lambda num: num % 2 == 0 or num % 3 == 0, numbers))
print(" ,".join(str(number) for number in filtered_numbers))