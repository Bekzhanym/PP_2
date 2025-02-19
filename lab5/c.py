import re
pattern = r"\b[a-z]+_[a-z]+\b"

text = ["bekzhan_bek","bekzh_daryn","BEKZHAN_DARYN","Nikita_Professor","dog_cat"]
for elem in text:
    if re.fullmatch(pattern,elem):
        print(f"Строка '{elem}' соответствует шаблону")
    else:
        print(f"Строка '{elem}' не соответствует шаблону")

#Write a Python program to find sequences of lowercase letters joined with a underscore.

