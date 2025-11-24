def occurs(number, array):
    return 'appears' if number in array else "does not appear"

arr = [15, 38, 7, 23, 14]
number = int(input("Number: "))

print("Array:", arr)
print(f"Result: number {number} {occurs(number, arr)} in the array")
