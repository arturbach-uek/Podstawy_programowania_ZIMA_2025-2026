def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

arrays = [
    [5, 2, 9, 1, 5],
    [10, 3, 8, 6],
    [4, 7, 1, 0, 9]
]

for arr in arrays:
    print("Original:", arr)
    print("Sorted:", bubblesort(arr.copy()))
    print()