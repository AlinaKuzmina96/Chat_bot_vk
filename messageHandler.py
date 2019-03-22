import os
import importlib
from Chat_bot_vk_2.command_system import command_list
from Chat_bot_vk_2.weather import weather
from Chat_bot_vk_2.search import search
import re
import vk_api

vk = vk_api.VkApi(token="0508fc8fa3c6b0ef98e56a11b7894ceeab39158b1a32fe21a744ac1660f1007c44f55bf4554098d3953a2")

vk._auth_token()

def load_modules():
   # путь от рабочей директории, ее можно изменить в настройках приложения
   files = os.listdir("D:\Python\Chat_bot_vk_2\commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

def get_answer(body):
    # Сообщение по умолчанию если распознать не удастся
    load_modules()
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    attachment = ''
    com = r"погода ([\w.-]*)"
    com1 = r"вопрос ([\w. ?]*)"
    if re.match(com, body):
        match = re.match(com, body)
        message = weather(match.group(1))
    elif re.match(com1, body):
        match = re.match(com1, body)
        message = search(match.group(1))
    else:
        for c in command_list:
            if body in c.keys:
                message, attachment = c.process()
    return message, attachment

def create_answer(body, id):
   message, attachment = get_answer(body.lower())
   vk.method("messages.send", {"peer_id": id, "message": message, "attachment": attachment})




