def fibonacci(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    
    prev, curr = 0, 1
    for _ in range(3, number + 1):
        prev, curr = curr, prev + curr
    return curr


print(fibonacci(5))
