def identity_matrix(n):
    matrix = [[0 for j in range(n)] for i in range(n)]
    
    for i in range(n):
        matrix[i][i] = 1
    
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

for size in [3, 5, 8]:
    print(f"Identity matrix {size}x{size}:")
    print_matrix(identity_matrix(size))
