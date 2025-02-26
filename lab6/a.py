
#Write a Python program with builtin function to multiply all the numbers in a list

from math import prod  # Встроенная функция для умножения элементов списка

def multi(numb):
    s.append(numb)  
    print(s)  
    print("Произведение всех чисел:", prod(s))  # Выводим произведение элементов списка

s = []  
n = int(input())  

for i in range(n):
    r = int(input())  # Ввод числа
    multi(r)  # Вызываем функцию
