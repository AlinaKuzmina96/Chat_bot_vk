from Chat_bot_vk_2 import command_system
import requests
import random

def image():
   attachment = get_random_wall_picture(data)
   message = 'Вот тебе картинка'
   return message, attachment

params = {
        'owner_id': -46053768,
        'album_id': 'wall',
        'count': 0,
        'access_token': '99832d7799832d7799832d772399e6e7ab9998399832d77c2fc24fc1ff5e21fef2cdbf6',
        'v': 5.80
}
api_url = "https://api.vk.com/method/photos.get?"
res = requests.get(api_url, params=params)
data = res.json()

def get_random_wall_picture(data):
    max_num = data["response"]['count']
    num = random.randint(1, max_num)
    params = {
        'owner_id': -46053768,
        'album_id': 'wall',
        'count': 1,
        'offset': num,
        'access_token': '99832d7799832d7799832d772399e6e7ab9998399832d77c2fc24fc1ff5e21fef2cdbf6',
        'v': 5.80}
    api_url = "https://api.vk.com/method/photos.get?"
    res = requests.get(api_url, params=params)
    data1 = res.json()
    photo = data1["response"]['items'][0]['id']
    attachment = 'photo' + str(-46053768) + '_' + str(photo)
    return attachment

image_command = command_system.Command()

image_command.keys = ['картинка']
image_command.description = 'Пришлю картинку'
image_command.com = "Напиши 'Картинка'"
image_command.process = image