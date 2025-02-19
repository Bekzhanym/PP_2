import re

# Исходная строка в CamelCase
camel_case_string = "ConvertCamelCaseToSnakeCase"

# Заменяем заглавные буквы на "_буква" и переводим в нижний регистр
snake_case_string = re.sub(r'(?<!^)([A-Z])', r'_\1', camel_case_string).lower()

# Вывод результата
print(snake_case_string)
