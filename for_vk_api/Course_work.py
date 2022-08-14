import requests
from pprint import pprint

class VkWorker:
    base_url = 'https://api.vk.com/method/'
    
    def __init__(self, token, version='5.131'):
        self.params = {'access_token': token,
                       'v': version
        }
    
    def profile_photo_get(self):
        method_url = self.base_url + 'photos.get'
        this_method_params = {'album_id': 'profile',
                              'extended': '1',
                              'count': '1000'
        }
        this_method_params.update(self.params)
        
        ans = (requests.get(method_url, params=this_method_params)).json()
        return ans
    
    def profile_photo_url_loader(self):
        name_url_dict = {}
        items_list = self.profile_photo_get()['response']['items']
        for item in items_list:
            if 'likes' in item:
                photo_name = item['likes']['count']
            if 'sizes' in item:
                sizes_list = item['sizes']
                height_list = []
                [height_list.append(height['height']) for height in sizes_list]
                max_height = max(height_list)
                for params in sizes_list:
                    if params['height'] == max_height:
                        name_url_dict[photo_name] = params['url']
                        
        return name_url_dict
                  
class YaWorker:
    base_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    
    def __init__(self, token):
        self.token = token
    
    def get_headers(self):
        return{
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def ya_uploader(self, Path_to_file: str, name_url_dict):
        method_url = self.base_url + 'upload'
               
        method_params = {'path': f'{Path_to_file}71',
                         'url': 'https://sun9-25.userapi.com/impg/c854528/v854528002/1aa31a/p1cU5y_Sabs.jpg?size=516x516&quality=96&sign=605156457c1fc26b83935edd101bca23&c_uniq_tag=dP613qL_jfwUnQ3sjm-qcOPbj6CzBildSTDzkqIcVbw&type=album',
                         'disable_redirects': 'false'
        }
        my_headers = self.get_headers()
        responce = requests.put(method_url, headers=my_headers, params=method_params)
        return responce.json()

                    
if __name__ == '__main__': 
    vk_token = "vk1.a.SqgE19qXn5AohCZg4bQP3vZ6XH3hiRbzh09Ta_nMQsXEbfNYHNGiXTCUmTEkU-ue_aXE-a6Ewg-lFtEw-elbBAMZUCaldZ3A8WPFxbSAPgRjy63hTZYu7fo9JmmtFyANuM0FTCmQn3BDBY-lxeRAk-kM8m8Mc5P_mVYMnnsJRZjdm3taI0tdq3HoLuIReE6l"
    ya_token ='https://sun9-24.userapi.com/impg/IqfUyMpzWVu2-yrl5VxpoRVcjll4PVHUWwGoGQ/ecXqGCodX68.jpg?size=1620x2160&quality=95&sign=8548e47ee1f6cdea5eb4dfd9f95fad17&c_uniq_tag=NUoT2iYrBSiEi4aWny6KXrU-5wi3jZPgspIxxqbLVzE&type=album'
    MyVkPhotos = VkWorker(vk_token)
    MyYaDisk = YaWorker(ya_token) 
    photo_url = 'https://sun9-25.userapi.com/impg/c854528/v854528002/1aa31a/p1cU5y_Sabs.jpg?size=516x516&quality=96&sign=605156457c1fc26b83935edd101bca23&c_uniq_tag=dP613qL_jfwUnQ3sjm-qcOPbj6CzBildSTDzkqIcVbw&type=album'
    responce = requests.get(photo_url)
    with open('Новый текстовый документ.txt', 'w') as f:
        f.write('responce')
    