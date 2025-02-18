import requests
import os
import time
import webbrowser
from datetime import datetime
date = datetime.now()
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))

def symbolPrint(str):
    for i in str:
        print(i, end="", flush=True)
        time.sleep(0.075)
    return ""

sys_ques = """SYS> Введите:
0. Выйти
1. Узнать дату и время
2. Узнать погоду
3. Открыть веб-сайт

"""
sys = "SYS> Что вы хотите сделать?\n\n"
sys_err = "\nSYS> Пожалуйста, уточните ваш запрос."
inputChar = "> "

symbolPrint(sys_ques)

while True:
    symbolPrint(sys)

    sys_input = input(inputChar)

    match sys_input:
        case "0":
            exit()
        case "1":
            symbolPrint(
f"""
SYS> Текущее время:
{date.hour}:{date.minute}
{date.day}.{date.month}.{date.year}

"""
)
        case "2":
            api_weather = input(symbolPrint("\nSYS> Введите свой API погоды (openweathermap.org)\n\n> "))
            city = input(symbolPrint("\nSYS> Введите название города\n\n> "))
            weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&APPID={api_weather}")

            if weather_data.json()['cod'] == '404':
                symbolPrint("\nSYS> Город не найден\n")
            elif weather_data.json()['cod'] == '401':
                symbolPrint("\nSYS> Неправильный API\n")
            else:
                cityName = weather_data.json()['name']
                weather = weather_data.json()['weather'][0]['description']
                temp = round(weather_data.json()['main']['feels_like'])
                tempFeel = round(weather_data.json()['main']['temp'])
                wind = weather_data.json()['wind']['speed']
                windDeg = weather_data.json()['wind']['deg']
                sunrise = datetime.fromtimestamp(weather_data.json()['sys']['sunrise']).strftime('%H:%M')
                sunset = datetime.fromtimestamp(weather_data.json()['sys']['sunset']).strftime('%H:%M')
                humidity = weather_data.json()['main']['humidity']

                symbolPrint(
f"""
SYS> Данные о погоде в городе {cityName}:
Температура воздуха: {temp}°C
Погода: {weather}
Ощущается как: {tempFeel}°C
Ветер: {wind} м/с
Направление ветра: {windDeg}
Влажность: {humidity}%
Восход: {sunrise}
Закат: {sunset}

"""
)
        case "3":
            typeUrl = input(symbolPrint("\nSYS> Что вы хотите найти?\n0. Выйти\n1. Веб-сайт\n2. Найти в поисковике\n\n> "))
            
            match typeUrl:
                case "0":
                    break
                case "1":
                    url = input(symbolPrint("\nSYS> Введите URL веб-сайта\n\n> "))
                    webbrowser.get('Chrome').open_new_tab(url)
                    print()
                case "2":
                    url = input(symbolPrint("\nSYS> Что вы хотите найти\n\n> "))
                    webbrowser.get('Chrome').open_new_tab('https://www.google.com/search?q={}'.format(url))
                    print()

        case _:
            symbolPrint(sys_err + sys)