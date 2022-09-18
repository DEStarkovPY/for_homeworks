from pprint import pprint

# Немного о функции sum:
list_a = [['a', 'b'], ['c', 'd']]
list_a = sum(list_a, []) # - второй аргумент функции sum - начальное значение, изначально равное 0.Заменив его, можно получить из вложенности полный результат
data = [
    [13, 23, 45, 36],
    [13, 35, 64, 24],
    [34, 42, 12, 56]
]

# List comprehension:
    # смысл в том, что все условия записываются в квадратных скобках [] в одну строку
[row[index] for index, row in enumerate(data)] # - получаем список из диагональных элементов
[{row[1] : row[0]} for row in data] # - получаем словарь с ключём по индексу 1 и значением по 2

people = {1: {'name': 'Oleg', 'age': '29', 'sex': 'Male'},
          2: {'name': 'Danil', 'age': '19', 'sex': 'Male'},
          3: {'name': 'Den', 'age': '17', 'sex': 'Male'}
}
round(sum([int(info.get('age')) for info in people.values()])/ len(people), 1)  # - получим средний возраст всех людей из словаря

stream = [
    'user1,3',
    'user4,7',
    'user3,8',
    'user4,2',
    'user2,4',
    'user5,10',
    'user3,2'
]

total_views_1 = sum([int(num[-1]) for num in stream])
total_views_2 = sum([int(el.split(',')[1]) for el in stream]) # - два способа подсчёта просмотров\
total_unique_users = len(set([el.split(',')[0] for el in stream])) # - вычисляем количество уникальных пользователей


# Args:
    # - арги работают таким образом, что сколько элементов не передали бы аргументом, они все упакуются в кортеж
    # Упаковка всех элементом в кортеж
dist_1 = {'flat_1': 10500, 'flat_2': 11000}
dist_2 = {'flat_3': 15000}
dist_3 = {'flat_4': 10500, 'flat_5': 10000, 'flat_6': 11000}

def ave_price(*districts): # - используем '*', чтобы активировать неограниченный ввод аргументов, для преообразования кортежа

    cost = 0
    counter = 0
    for dist in districts:
        cost += sum(dist.values())
        counter += len(dist.values())

    return round(cost/counter, 1)

ave_price(dist_1, dist_2, dist_3)




# Kwargs:
    # - кварги работают таким образом, что сколько элементов не передали бы аргументом, они все упакуются в словарь
{**dist_1, **dist_2, **dist_3}

# Функция map (высшего порядка):
    # - принимает в качестве аргуметов название функции и итерируемый объект, для того, чтобы исполнить её к каждому элементу итерир объекта

import numpy as np # - способ импортирования библиотеки как 'np'
prices = [[13, 23, 45, 36], [13, 45, 36], [13, 23]]
list(map(lambda argument: sum(argument)/len(argument), prices)) # - считает среднее арифметическое по каждому вложенному списку в prices
    # синтаксис lambda-функции: lambda арумент: условие

list(map(np.mean, prices)) # - функция 'np.mean' находит среднее значение по чему-либо



# Функция filter (высшего порядка):
     # -  принимает в качестве аргуметов название функции и итерируемый объект, для того, чтобы исполнить её к удовлетворяющему условия элементам итерир объекта (по True/False)
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Москва', 'Россия']},
    {'visit4': ['Париж', 'Франция']}
]

def Rv_finder(vist_list):
    return list(filter(lambda visit: 'Россия' in list(visit.values())[0] ,geo_logs)) # - создание нового списка, вмещающего только визиты в Россию
Rv_finder(geo_logs)


# Функция sorted:
    # Синтаксис: sorted(итерируемый объект, key=(правило сортировки))

dist_4 = {'flat_4': 10500, 'flat_5': 10000, 'flat_6': 11000}
print(dict(sorted(dist_4.items(), key= lambda item: item[1]))) # - сортировка по возрастанию цены


# Функция reduce (высшего порядка):
    # -
