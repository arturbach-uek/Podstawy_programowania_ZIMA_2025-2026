import math
circumfence = float(input("Enter tree circumference in cm: "))
diameter = circumfence / math.pi
can_be_cut = diameter >= 50
print(f"Tree can be cut down: {can_be_cut}")