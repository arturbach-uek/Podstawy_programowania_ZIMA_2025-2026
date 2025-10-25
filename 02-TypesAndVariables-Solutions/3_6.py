from math import sqrt

h = float(input("Enter height in meters: "))
d = 3.57 * sqrt(h)

print("Distance to the horizon:", round(d, 2), "km")