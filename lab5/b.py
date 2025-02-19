import re

pattern = r"ab{2,3}"
text = ["ab", "abb", "abbb","abbbb","abbbbb"]

for element in text:
    if re.fullmatch(pattern, element):
        print(f"Строка '{element}' соответствует шаблону!")
    else:
        print(f"Строка '{element}' НЕ соответствует шаблону.")
#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.



