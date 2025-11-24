array = [
    [-38, 19], 
    [5, 40], 
    [-7, 11], 
    [29, 16]
]

min_val = max_val = array[0][0]
min_pos = max_pos = (0, 0)

for i, row in enumerate(array):
    for j, val in enumerate(row):
        if val < min_val:
            min_val = val
            min_pos = (i, j)
        if val > max_val:
            max_val = val
            max_pos = (i, j)

print(f"Smallest value: {min_val} at row {min_pos[0]}, column {min_pos[1]}")
print(f"Largest value: {max_val} at row {max_pos[0]}, column {max_pos[1]}")
