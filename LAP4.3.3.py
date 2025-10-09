import math

n = 4   # number of sides
s = 25  # length of a side
area = (n * s**2) / (4 * math.tan(math.pi / n))
print("Area of polygon:", area)
