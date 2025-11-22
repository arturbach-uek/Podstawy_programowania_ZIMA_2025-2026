arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4, 5]

is_subset = True

for element in arr1:
    if element not in arr2:
        is_subset = False
        break

if is_subset:
    print("The first array is a subset of the second array.")
else:
    print("The first array is NOT a subset of the second array.")
