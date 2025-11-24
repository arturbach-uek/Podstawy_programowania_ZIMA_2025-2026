def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = []
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

matrices = [
    [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ],
    [
        [1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 0]
    ],
    [
        [5, 6, 7, 8]
    ]
]

for mat in matrices:
    print("Original matrix:")
    print_matrix(mat)
    print("Transposed matrix:")
    print_matrix(transpose_matrix(mat))
