def second_largest(arr):
    if len(arr) < 2:
        return None

    largest = second = arr[0]
    for num in arr[1:]:
        if num > largest:
            second, largest = largest, num
        elif num > second and num != largest:
            second = num
    return second

def range_difference(arr):
    smallest = largest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return largest - smallest

def median(arr):
    sorted_arr = arr[:]

    for i in range(len(sorted_arr)):
        for j in range(i+1, len(sorted_arr)):
            if sorted_arr[i] > sorted_arr[j]:
                sorted_arr[i], sorted_arr[j] = sorted_arr[j], sorted_arr[i]

    n = len(sorted_arr)
    mid = n // 2
    return sorted_arr[mid] if n % 2 == 1 else (sorted_arr[mid-1] + sorted_arr[mid]) / 2

def min_max(arr):
    smallest = largest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return [smallest, largest]

def array_to_string(arr):
    result = ""
    for i, num in enumerate(arr):
        result += str(num)
        if i != len(arr) - 1:
            result += "-"
    return result
