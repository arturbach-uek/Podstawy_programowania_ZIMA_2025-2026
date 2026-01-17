from functools import reduce

numbers = [1,2,3,4,5]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)

numbers = [2,4,6,3,7,5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
sum_even = reduce(lambda x, y: x + y, even_numbers)
print(sum_even)
