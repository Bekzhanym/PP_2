#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def pal(palin):
    if palin == palin[::-1]:  # Сравниваем строку с её реверсированной версией
        return "Yes"
    else:
        return "No"

r = input("Введите строку: ")  # Ввод строки
print(pal(r))  # Вывод результата
