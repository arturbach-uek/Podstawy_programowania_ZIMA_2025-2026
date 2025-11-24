def create_2d_arr(x, y):
    arr = []
    for rows in range(x):
        row = []
        for cols in range(y):
            row.append(0)
        arr.append(row)
    return arr

print(create_2d_arr(3, 5))

