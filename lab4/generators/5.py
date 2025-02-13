def reverse(n):
    """Generator that yields numbers from n down to 0."""
    for i in range(n, -1, -1):  # Iterate from n to 0
        yield i

# Get user input
n = int(input("Enter a number: "))

# Test the generator
for num in reverse(n):
    print(num)
