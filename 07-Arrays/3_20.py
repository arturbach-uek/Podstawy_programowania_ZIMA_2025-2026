arr = [7, 9, 2, 4, 5, 6]
odd_arr = [number for number in arr if number % 2 == 0]
even_arr = [number for number in arr if number % 2 != 0]
print(odd_arr + even_arr)
