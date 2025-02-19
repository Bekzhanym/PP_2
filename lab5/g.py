import re

# Исходная строка в snake_case
snake_case_string = "hello_world_python"

# Разбиваем строку по символу "_"
words = snake_case_string.split("_")

# Преобразуем каждое слово, делая первую букву заглавной
camel_case_string = "".join(word.capitalize() for word in words)

print(camel_case_string) 
