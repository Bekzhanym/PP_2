import re 
text = ["5000tg", "Discount:10%"]
pattern = r"^\b[0123]+_\b"
for elem in text:
    if re.fullmatch(pattern,elem):
        print(f"Строка '{elem}' соответствует шаблону")
    else:
        print(f"Строка '{elem}' не соответствует шаблону")