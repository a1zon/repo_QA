import os.path

CUR_FILE = (os.path.abspath('hello.txt')) # только уникальный файл
CUR_DIR = (os.path.dirname(CUR_FILE)) # папка, в которой лежит файл

TMP_DIR = os.path.join(CUR_DIR, 'tmp') # папка tmp в папке с файлом
print(TMP_DIR)