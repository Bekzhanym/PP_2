import math

def regular_polygon_area(n, s):
    """Calculate the area of a regular polygon given the number of sides and the length of a side."""
    return (n * s**2) / (4 * math.tan(math.pi / n))

# Taking user input
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

# Calculating and printing the area
print("The area of the polygon is:", round(regular_polygon_area(n, s), 2))
