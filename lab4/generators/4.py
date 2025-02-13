def square(a,b):
    for i in range(a,b+1):
        
        yield i**2

start, end = 1, 5
for num in square(start, end):
    print(num)
