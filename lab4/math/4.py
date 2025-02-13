def parallelogram_area(base, height):
    """Calculate the area of a parallelogram given base and height."""
    return base * height

# Taking user input
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

# Calculating and printing the area
print("Expected Output:", parallelogram_area(base, height))
