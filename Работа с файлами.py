import os # - библиотека для работы с путями
this_path = os.getcwd() # - получить абсолютный путь к текущ. каталогу
#os.path.join(path, *path) - получение платформоспецифичного пути
#os.path.dirname(path) - абсолютный путь до каталога
#os.path.basename(path) - имя файла

file_name = 'test.txt'
full_path_test_file = os.path.join(this_path, file_name )




with open ('test.txt') as file: # - открытие файла без последующего закрытия (автоматическое закрытие)
    data = file.read()
    pass                        # - 'with' - контекстный менеджер
    
#read - чтение файла целиком
#readline - чтение файла построчно
#readlines - чтение всех строк в список

with open ('test.txt', 'at') as mod_file: # - 'r' - режим работы с файлом, необязательные аргумент в функции open(Имя файла, режим доступа + режим записи/чтения)
    mod_file.write( '\nHello, world\n')
    mod_file.write('I`m starting developer!')
# Режими доступа:
# 'r' (по-умолчанию) - чтение файла (read)
# 'w' - запись в файл (write)
# 'a' - запись в конец файла (append)
# Режими чтения/записи:
# 'b' - двоичный режим (работа с байтами)
# 't' (по-умолчанию) - текстовый режим
    pass

file_obj = open('test.txt') # - способ открытия и работы с файлом с закрытием
data = file_obj.read()
for line in file_obj:
    line.strip() # - метод, позволяющий убрать промежутки при чтении/записи файла (обрезает '\n')
file_obj.close()

# Кодировки:
with open (full_path_test_file, 'w', encoding = 'utf-8') as encod_test_file:
    encod_test_file.write('Hello!')
    # Windows: cp1251
    # Linux: utf-8


str('Ананасы | 10 | кг').replace('|', "") # - метод, позвоялющий заменить первый аргумент на второй в строчке
str('PY STR INT').split() # - метод, позволяющий получить список из строчки
','.join(['Hello', 'world']) # - выведет строку с запятой между словами