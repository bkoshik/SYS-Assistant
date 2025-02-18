import requests
from datetime import datetime
from minidefs import symbolPrint

def weather(api):
    city = input(symbolPrint("\nSYS> Введите название города\n\n> "))
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&APPID={api}")

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
Направление ветра: {windDeg}°
Влажность: {humidity}%
Восход: {sunrise}
Закат: {sunset}

"""
)