#Write a Python program to copy the contents of a file to another file
def copy_file(source, destination):
    with open(source, "r") as src, open(destination, "w") as dest:
        dest.write(src.read())

# Укажите файлы
source_file = "source.txt"  # Исходный файл
destination_file = "copy.txt"  # Куда копировать

copy_file(source_file, destination_file)
print("Файл успешно скопирован!")
