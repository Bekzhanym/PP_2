import re

pattern = r"^ab*"
text = ["ab", "abb", "abbb", "ba", "bba"]

for element in text:
    if re.fullmatch(pattern, element):
        print(f"Строка '{element}' соответствует шаблону!")
    else:
        print(f"Строка '{element}' НЕ соответствует шаблону.")
#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

