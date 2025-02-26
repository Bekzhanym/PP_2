import os

def delete_file(file_path):
    if os.path.exists(file_path):  # Проверяем, существует ли файл
        if os.access(file_path, os.W_OK):  # Проверяем, есть ли права на запись (удаление)
            os.remove(file_path)
            print(f"Файл '{file_path}' успешно удалён.")
        else:
            print(f"Нет доступа для удаления '{file_path}'.")
    else:
        print(f"Файл '{file_path}' не существует.")

# Укажите путь к файлу
file_path = input("Введите путь к файлу: ")
delete_file(file_path)
