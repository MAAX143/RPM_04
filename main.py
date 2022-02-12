import os

def input_path():
    pass

def dictionary(path):
    for filename in os.listdir(path): # Просматриваем файлы в папке
        pathfile = os.path(path, dict) # Записываем путь к файлу в директории
        dict[pathfile] = os.path.getsize(pathfile) # Записываем в словарь ключ - путь к файлу, значение - размер файла
        if os.path.isdir(pathfile): # Проверяем, является ли файл папкой, если да, то...
            dictionary(pathfile) # то снова запускаем функцию на проверку файлов в данной папке

def duplucate():
    pass

def output():
    pass