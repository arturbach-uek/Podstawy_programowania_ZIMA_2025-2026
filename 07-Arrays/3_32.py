matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before swap:")
for row in matrix:
    print(row)
    
matrix[0], matrix[-1] = matrix[-1], matrix[0]

print("\nAfter swap:")
for row in matrix:
    print(row)
