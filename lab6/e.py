def check_all_true(tup):
    return all(tup)  # Проверяем, являются ли все элементы истинными

# Пример кортежей
t1 = (1, 2, 3, True)  
t2 = (1, 0, 3, True)  

print(check_all_true(t1))  # Вывод: True
print(check_all_true(t2))  # Вывод: False
#all function
#0 is not true