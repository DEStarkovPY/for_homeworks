
import os
THIS_PATH = os.getcwd()
FILE_NAME_DEMO = 'demo.txt'
full_path_demo = os.path.join(THIS_PATH,FILE_NAME_DEMO)
FILE_NAME_1 = "file1.txt"
FILE_NAME_2 = "file2.txt"
FILE_NAME_3 = "file3.txt"
FILE_NAME123 = 'file123.txt'
full_path_1 = os.path.join(THIS_PATH,FILE_NAME_1)
full_path_2 = os.path.join(THIS_PATH,FILE_NAME_2)
full_path_3 = os.path.join(THIS_PATH,FILE_NAME_3)
full_path123 = os.path.join(THIS_PATH, FILE_NAME123)

print(' \nЗадание №1\n')
cook_book = {}
def cook_book_creature(file_name):
    with open(file_name, encoding = 'utf-8') as cb_file:
        for line in cb_file:
            dish_ingridients = []
            dish_name = line.strip()
            ing_num = cb_file.readline().strip()
            for ing_id in range(int(ing_num)):
                ing_items = cb_file.readline().strip().replace('|', "")
                ing_items_list = ing_items.split()
                if len(ing_items_list) == 3:
                    ing_dict = {'ingredient_name': ing_items_list[0], 'quantity': ing_items_list[1], 'measure': ing_items_list[2]}
                    dish_ingridients.append(ing_dict)
                    cook_book[dish_name] = dish_ingridients
                elif len(ing_items_list) == 4:
                    ing_dict = {'ingredient_name': ' '.join(ing_items_list[0:2]), 'quantity': ing_items_list[2], 'measure': ing_items_list[3]}
                    dish_ingridients.append(ing_dict)
                    cook_book[dish_name] = dish_ingridients
            cb_file.readline()        
    return print(cook_book)

cook_book_creature(full_path_demo)

print(' \nЗадание №2\n')

def get_shop_list_by_dishes(dishes, person_count):
    all_ing_dict = {}
    for dish in cook_book.keys():
        if dish in dishes:
            for item in cook_book.get(dish):
                all_ing_dict[item['ingredient_name']] = {'measure' : item['measure'] , 'quantity' : int(item['quantity']) * int(person_count)}  
        else:
            None
    return print(all_ing_dict)

get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински'], 5)


print('\nЗадание №3\n')

def file_len_finder(file_name1, file_name2, file_name3):
    string_val_dict = {}
    with open (file_name1, encoding = "utf-8") as file_1:
        string_len1 = 0
        for string in file_1:
            string_len1 += 1
        file_1.seek(0,0)
        text_1 = file_1.read()
        string_val_dict[string_len1] = [text_1, file_name1]
    with open (file_name2, encoding = "utf-8") as file_2:
        string_len2 = 0
        for string in file_2:
            string_len2 += 1
        file_2.seek(0,0)
        text_2 = file_2.read()
        string_val_dict[string_len2] = [text_2, file_name2]
    with open (file_name3, encoding = "utf-8") as file_3:
        string_len3 = 0
        for string in file_3:
            string_len3 += 1 
        file_3.seek(0,0)
        text_3 = file_3.read()
        string_val_dict[string_len3] = [text_3, file_name3]
    return string_val_dict
    


def file_writer(file_len_dict, writer_file):
    sorted_file_tuple = sorted(file_len_dict.items(), key=lambda x: x[0])
    sorted_file_dict = dict(sorted_file_tuple)
    with open(writer_file, 'a', encoding = "utf-8") as file_123:
        for key, value in sorted_file_dict.items():
            file_123.write(f'{str(value[1])}\n')
            file_123.write(f'{str(key)}\n')
            file_123.write(f'{value[0]}\n')
            
    return print(f' Запись в файл: {writer_file} завершена успешно!')
            
        
                
        
        
        
file_writer(file_len_finder(full_path_1, full_path_2, full_path_3), full_path123)