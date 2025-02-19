#Write a Python program to insert spaces between words starting with capital letters.
import re

# Исходная строка
text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"

# Вставляем пробел перед заглавными буквами (кроме первой)
result = re.sub(r'(?<!^)([A-Z])', r' \1', text)

# Вывод результата
print(result)
