#Create a generator that generates the squares of numbers up to some number N.
class Squares:
    def __init__(self, N):
        self.N = N
        self.a = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.N:  # Если число больше N, остановить итерацию
            raise StopIteration
        result = self.a ** 2  # Возвращаем квадрат числа
        self.a += 1  # Увеличиваем число
        return result

# Используем генератор
N = 5
for num in Squares(N):
    print(num)
