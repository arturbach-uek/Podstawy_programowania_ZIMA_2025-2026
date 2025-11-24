###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print("Number of elements: ", len(arr))
print("First value: ", arr[0])
print("Second value: ", arr[1])
print("Last value: ", arr[-1])
print("Last but one value: ", arr[len(arr) - 2])
print("Sum of 1st and last: ", arr[0] + arr[-1])
print("Middle value: ", arr[len(arr) // 2])
print("All values separated by a single space: ", end="")
for i in range(len(arr)):
    print(arr[i], end=" ")