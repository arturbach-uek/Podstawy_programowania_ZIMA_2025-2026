matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print("Before swap:")
for row in matrix:
    print(row)
    
for row in matrix:
    row[0], row[-1] = row[-1], row[0]

print("\nAfter swap:")
for row in matrix:
    print(row)
