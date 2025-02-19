#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
pattern = r"\ba.*b\b"

text = ["ab","as   56565 &$-_ fdb","basfa","alokmb"]
for elem in text:
    if re.fullmatch(pattern,elem):
        print(f"Строка '{elem}' соответствует шаблону")
    else:
        print(f"Строка '{elem}' не соответствует шаблону")

