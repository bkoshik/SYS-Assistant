import requests
import selenium
from datetime import *
date = datetime.now()

sys_ques = """SYS> Введите:
0. Выйти
1. Узнать дату и время
2. Узнать погоду
3. Открыть веб-сайт

SYS> Что вы хотите сделать?
"""

print(sys_ques)

sys_input = int(input("> "))

match sys_input:
    case 0:
        exit()
    case 1:
        print(f"\n{date.hour}:{date.minute}\n{date.day}.{date.month}.{date.year}")
    case 2:
        api_weather = input("\nSYS> Введите свой API погоды\n\n> ")
        city = input("\nSYS> Введите название города\n\n> ")
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&APPID={api_weather}")

        if weather_data.json()['cod'] == '404':
            print("No City Found")
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

            print(f'\nНазвание города: {cityName}\n'
                f'Температура воздуха: {temp}°C\n'
                f'Погода: {weather}\n'
                f'Ощущается как: {tempFeel}°C\n'
                f'Ветер: {wind} м/с\n'
                f'Направление ветра: {windDeg}\n'
                f'Влажность: {humidity}%\n'
                f'Восход: {sunrise}\n'
                f'Закат: {sunset}')
    case 3:
        None
    case _:
        print("\nSYS> Пожалуйста, уточните ваш запрос.\n\nSYS> Что вы хотите сделать?")