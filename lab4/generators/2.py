#Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

class Even:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

# Получение ввода от пользователя
try:
    n = int(input("Введите число n: "))
    if n < 0:
        raise ValueError("n должно быть неотрицательным.")
except ValueError as e:
    print(f"Ошибка ввода: {e}")
else:
    even_numbers = Even(n)
    even_list = list(even_numbers)
    print(", ".join(map(str, even_list)))
