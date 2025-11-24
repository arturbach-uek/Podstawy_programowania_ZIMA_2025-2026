import matplotlib.pyplot as plt
import math

angles = list(range(0, 361))
y_values = [math.sin(math.radians(angle)) for angle in angles]

plt.plot(angles, y_values)
plt.title("y = sin(x) for x in 0-360 degrees")
plt.xlabel("Angle (degrees)")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
