import random

def rand_elem(array):
    index = random.randint(0, len(array) - 1)
    return array[index]

arr = [10, 20, 30, 40, 50]

print("Random element 1:", rand_elem(arr))
print("Random element 2:", rand_elem(arr))
print("Random element 3:", rand_elem(arr))
