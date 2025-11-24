arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

result = [number for number in arr1 if number not in arr2]

print("Numbers in first array not in second array:", result)
