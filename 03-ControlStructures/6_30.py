rows = 7 
cols = 7

for i in range(1, rows + 1):
    for j in range(cols):
        num = i + j * rows
        print(num, end=" ")
    print()
