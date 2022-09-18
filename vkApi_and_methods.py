# ID приложения: 8233250
import os
import requests
import time # - для установки задержки на исполнение запросов
from pprint import pprint
url = "https://oauth.vk.com/authorize?client_id=8233250&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=stats,offline&response_type=token&v=5.131" # - под ключом 'scope' находятся права доступа для токена пользователя (только нужные, перечисленные через запятую)


THIS_PATH = os.getcwd()
TOKEN_FILE_NAME = 'myToken.txt'
full_path = os.path.join(THIS_PATH, TOKEN_FILE_NAME)

with open(full_path, 'r', encoding='utf-8') as token_file:
    token = token_file.read().strip()
    
method_url = 'https://api.vk.com/method/users.get' # - метод получения расширенной информации по id 
my_params = {'user_ids' : '2',
             'access_token' : token,
             'v' : '5.131',
             'fields' : 'education, sex' # -дополнительные параметры (указаны в api-vk)
} 

# res = requests.get(method_url, params=my_params)
# pprint(res.json())


def search_groups(q: str, sorting=0, your_count=1000): 
    search_method_url = 'https://api.vk.com/method/groups.search' # - Осуществляет поиск сообществ по заданной подстроке
    search_params={
        'q' : q,
        'access_token' : token,
        'v' : '5.131',
        'sort' : sorting,
        'count' : your_count
    }
    ans = (requests.get(search_method_url, params=search_params).json())
    ans = ans['response']['items'] # - дабавляем два ключа, чтобы не видеть ненужную информацию 
    return ans

groups_json = search_groups('Python', 0, 10)

def getById_groups(groups_dict_json):
    method_url = 'https://api.vk.com/method/groups.getById' # - Возвращает информацию о заданном сообществе или о нескольких сообществах (Расширенную).
    groups_id_list = ','.join([str(group['id']) for group in groups_dict_json])
    getById_params = {'access_token' : token,
              'v' : '5.131',
              'group_ids' : groups_id_list,
              'fields' : 'members_count,activity'
    }
    
    ans = (requests.get(method_url, params=getById_params).json())
    ans = ans['response']
    return ans

groups_inf = getById_groups(groups_json)

#Реализация классов по API

class VkUser:
    base_url = 'https://api.vk.com/method/'
    
    def __init__(self, token, version='5.131'):
        self.params = {'access_token': token,
                       'v': version
        }
        
    def user_get(self, fields=None):
        method_url = self.base_url + 'users.get'
        self.params['fields'] = fields
        return (requests.get(method_url, params=self.params)).json()
    
    def search_groups(self, q, sorting=0, count=2):
        method_url = ''.join([self.base_url, 'groups.search'])
        this_method_params = {'q': q,
                              'sort': sorting,
                              'count': count
        }
        this_method_params.update(self.params)
        return (requests.get(method_url, this_method_params)).json()
    
if __name__ == '__main__':    
    VkApp = VkUser(token)
    VkApp.user_get()
    VkApp.search_groups('Python')
            
    