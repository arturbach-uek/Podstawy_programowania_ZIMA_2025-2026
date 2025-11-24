def flatten_2d_array(arr):
    return [elem for row in arr for elem in row]

arrays_2d = [
    [
        [2, 3], 
        [1, 5]
    ],
    [
        [5, 0, 3, 7, 5], 
        [9, 0, 9, 1, 2]
    ],
    [
        [2, 1], 
        [3, 5], 
        [7, 4], 
        [2, 6]
    ]
]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

for arr in arrays_2d:
    print("2D array:")
    print_matrix(arr)
    print("Flattened 1D array:", flatten_2d_array(arr))
