import os

out = input("Введите часть для удаления из названия файлов >>> ")

i = len(os.listdir())
while i>0:
    for file in os.listdir():
        os.rename(file, file.replace(out,""))
    i=-1
