numbers = [number for number in range(1, 21)]
third_powers = list(map(lambda num: num**3, numbers))
print(" ,".join(str(n) for n in third_powers))