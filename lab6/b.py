def low(numb):
    lower = []  
    upper = []  
    
    for char in numb:  # Перебираем символы строки
        if char.isupper():  
            upper.append(char)  
        elif char.islower():  
            lower.append(char) 
    
    return lower, upper  

r = input("Введите строку: ")  

lower, upper = low(r)  # Вызываем функцию и получаем списки

print("Lower:", lower)  # Вывод строчных букв
print("Upper:", upper)  # Вывод заглавных букв
