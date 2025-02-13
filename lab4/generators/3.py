#Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

class Div:
    def __init__(self,n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.current>self.n):
            raise StopIteration
        result = self.current
        self.current += 12
        return result
    
try:
    n = int(input("Введите число n: "))
    if n < 0:
        raise ValueError("n должно быть неотрицательным.")
except ValueError as e:
    print(f"Ошибка ввода: {e}")
else:
    even_numbers = Div(n)
    even_list = list(even_numbers)
    print(", ".join(map(str, even_list)))