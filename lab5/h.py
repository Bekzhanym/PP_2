import re

# Исходная строка
text = "HelloWorldPythonBekzhan"

# Разбиваем строку по заглавным буквам
words = re.split(r'(?=[A-Z])', text)

# Вывод результата
print(words)
