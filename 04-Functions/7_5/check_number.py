import range_check

number = int(input("A number: "))
x = int(input("Range start: "))
y = int(input("Range end: "))

result = range_check.in_range(number, x, y)

answer = "yes" if result else "no"
print(f"Number {number} in the range <{x},{y}>: {answer}")
