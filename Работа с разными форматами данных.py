#Формат CSV - обычные таблицы эксель. Итеррируемый объект, разбитый запятыми:
#Десереализация - разборка файла в байты для сериализации
#Сериализация - сборка байтов некоторый объект
import csv
import os
THIS_PATH = os.getcwd()
FILE_NAME = 'addresses.csv'
addresses_path = os.path.join(THIS_PATH,FILE_NAME)

with open(addresses_path) as file:
    #Десериализация в список:
    reader_list = csv.reader(file)
    #Десериализация в список:
    reader_dict = csv.DictReader(file)
     
    #Десериализация в случае, если объём файла небольшой (~100мб)
    news_list = list(reader_list)
    header = news_list.pop(0) # - первая строка таблицы 
    for row in news_list:
        row[-1]
    len(news_list)-1
  
#Сериализация:
with open('filesnewsafr.csv', 'w', encoding= 'utf-8') as f:
    writer = csv.writer(f, delimiter = ',', quoting = csv.QUOTE_MINIMAL) # - позволяет записать в csv-файл, аргумент "delimiter" отвечает за тот элемент, который разделяет значения в списке
    #csv.QUOTE_MINIMAL - Расстановка ковычек только там, где нужно
    #csv.QUOTE_ALL - Расстановка ковычек везде
    #csv.QUOTE_NONE, escapechar (r'\' или '\\')=  - Без ковычек
    writer.writerows(news_list) #- Позвоялет сериализовать все данные
    writer.writerow(header) #- Позволяет сериализовать одну строку
# csv.register_dialect() # - настройки форматирования

csv.register_dialect('customcsv', delimiter = ' ', quoting = csv.QUOTE_NONE, escapechar = '\\') # - метод, позволяющий сохранить настройки для записи в файл
#with open('filesnewsafr.csv', 'customcsv')




#Формат JSON - формат-словарь:
import json
from pprint import pprint # - получение prettyprint, получающее более удобное представление словаря

with open('test.json', encoding = 'utf-8') as json_file:
    json_data = json.load(json_file) # - функция десериализации всего json-файла
    #json_str = json.loads(str) - десериализация из строки
news_list_j = json_data



with open('testwrite.json', 'w', encoding = 'utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii = False, indent = 4) # - функция записи в json-файл (аргументы: текст записи, файл для записи, нормальный русский язык в файле, включены отступы)
    #json.dumps() - сериализация построчно
    



#Формат YAML - прородитель json, похожий, но менее инвариантный (более локаничный)

# import yaml
# with open('test.yaml', encoding = 'utf-8') as yaml_file:
#     yaml_data = yaml.load(yaml_file) # - функция десериализации всего json-файла
#     #yaml_str = yaml.loads(str) - десериализация из строки
# news_list_y = yaml_data
# pprint(news_list_y)


# with open('test.yaml', 'w', encoding = 'utf-8') as yaml_file:
#     yaml.dump(yaml_data, yaml_file, allow_unicode = True, default_flow_style = False) # - функция записи в json-файл (аргументы: текст записи, файл для записи, нормальный русский язык в файле, включены отступы)
#     #yaml.dumps() - сериализация построчно




#Формат XML - формат клиент-серверного взаимодействия, родитель 'html':

import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding = 'utf-8') # - передача кодировки для чтения вторым аргументом в метод .parse
tree = ET.parse('test.xml', parser) # - получение xml-файла для работы с ним 
xml_root = tree.getroot() #- получение корня файла
xml_root.tag
xml_root.text # - получение атрибутов по заголовкам в файле
book_list = xml_root.findall('catalog/book') # - найти все book
#book_list = xml_root.find('catalog/book') # - найти первую book
for book in book_list:
    (book.find('title').text)
    (book.text)
