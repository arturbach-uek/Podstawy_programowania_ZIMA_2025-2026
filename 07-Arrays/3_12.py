arr = [2, 3, 2, 5, 8, 1, 9, 8]

unique_elements = []
for x in arr:
    if arr.count(x) == 1:
        unique_elements.append(x)

print("Array:", arr)
print("Unique elements:", unique_elements)
