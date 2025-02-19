#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
pattern = r"\b[A-Z][a-z]+\b"

text = ["bA","qALAN","Bekzhan","bEk","Bek","Be","Ko"]
for elem in text:
    if re.fullmatch(pattern,elem):
        print(f"Строка '{elem}' соответствует шаблону")
    else:
        print(f"Строка '{elem}' не соответствует шаблону")



