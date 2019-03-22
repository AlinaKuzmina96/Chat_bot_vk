from Chat_bot_vk_2 import command_system
import re, urllib
from urllib import request

def parse():
    s = 'https://russian.rt.com/news'
    doc = urllib.request.urlopen(s).read().decode('utf-8', errors='ignore')
    doc = doc.replace('\n', '')
    zagolovki = re.findall('<a class="link link_color" href="(.+?)</a>', doc)
    site = 'https://russian.rt.com'
    dict = {}
    message = ""
    zagolovki = zagolovki[::2]
    for x in zagolovki:
        news = site + str(x.split('">')[0])
        dict[x.split('">')[1].strip()] = news
    for key, value in dict.items():
        if len(message + key + '\n' + value + '\n \n') < 4096:
            message = message + key + '\n' + value + '\n \n'
    return message, ''

parse_command = command_system.Command()

parse_command.keys = ['новости']
parse_command.description = 'Покажу список последних новостей'
parse_command.com = "Напиши 'Новости'"
parse_command.process = parse

