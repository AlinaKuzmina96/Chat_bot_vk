import requests
from translate import Translator

def weather(city):
    translator= Translator(to_lang="en", from_lang="ru")
    tran_city = translator.translate(city)
    api_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': str(tran_city),
        'appid': '74022e35bc3740bd98b746f9cca0a49c',
        'units': 'metric',
        'lang': 'ru'
        }
    params1 = {
        'q': "london",
        'appid': '74022e35bc3740bd98b746f9cca0a49c',
        'units': 'metric',
        'lang': 'ru'
        }
    res = requests.get(api_url, params=params)
    res1 = requests.get(api_url, params=params1)
    data = res.json()
    data1 = res1.json()
    if city == 'лондон':
        message = "Температура на данный момент: " + str(data1['main']['temp'])
    else:
        message = "Температура на данный момент: " + str(data['main']['temp'])
    return message