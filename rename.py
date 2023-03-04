import os

out = input("Введите часть для удаления из названия файлов >>> ")

for file in os.listdir():
    os.rename(file, file.replace(out,""))