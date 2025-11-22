arr = [
    [7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]
]

last_column_index = len(arr[0]) - 1
sum_last_col = 0

for row in arr:
    sum_last_col += row[last_column_index]

print("Sum of last column:", sum_last_col)
