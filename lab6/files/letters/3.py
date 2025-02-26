import os

path = r'C:\Users\bekzh\Desktop\flutter\flutter_application_1\android'


if os.path.exists(path):
    print("Путь существует!")
    print("Каталог:", os.path.dirname(path))  # Получаем путь до каталога
    print("Имя файла:", os.path.basename(path))  # Получаем имя файла
else:
    print("Путь не найден.")

