x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x == 0 and y == 0:
    location = "at the origin (0,0)"
elif x == 0:
    location = "on the Y-axis"
elif y == 0:
    location = "on the X-axis"
elif x > 0 and y > 0:
    location = "in the first quadrant"
elif x < 0 and y > 0:
    location = "in the second quadrant"
elif x < 0 and y < 0:
    location = "in the third quadrant"
elif x > 0 and y < 0:
    location = "in the fourth quadrant"

print(f"Point P({x},{y}) is {location} of the coordinate system")
