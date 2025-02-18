import requests, time, webbrowser, os, keyboard
import math # Для 4 варианта
from datetime import datetime
date = datetime.now()
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))

print("\033[38;2;0;180;0m")

def symbolPrint(str):
    for i in str:
        print(i, end="", flush=True)
        # time.sleep(0.1)
    return ""

sys_ques = """SYS> Введите:
0. Выйти
1. Узнать дату и время
2. Узнать погоду
3. Открыть веб-сайт
4. Ввести python-команды
5. Секундомер/Таймер

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
{date.hour:02}:{date.minute:02}
{date.day:02}.{date.month:02}.{date.year}

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
        case "4":
            startCom = input(symbolPrint("\nSYS> Хотите начать? (для завершения вводите END)\n0. Выйти\n1. Начать однострочное\n2. Начать многострочное\n3. Пройти обучение\n\n> "))

            match startCom:
                case "0":
                    break
                case "1":
                    while True:
                        try:
                            lineOneCode = input("\n>>> ")
                            if lineOneCode == "END":
                                break
                            result = eval(lineOneCode)
                            symbolPrint(str(result))
                        except Exception as e:
                            print(f"Ошибка: {e}")
                case "2":
                    code = ""
                    print()
                    while True:
                        lineManyCode = input(">>> ")
                        if lineManyCode == "END":
                            break
                        code += lineManyCode + "\n"

                    try:
                        exec(code)
                    except Exception as e:
                        print(f"Ошибка: {e}")
                case "3":
                    symbolPrint(
"""
SYS> Аргументы:
    Первый аргумент expression:
        Когда мы вызываем eval(), содержание expression воспринимается интерпретатором как выражение Python.

        Запрещены:
            if/elif/else
            def/class
            for/while
            import
    
    Второй аргумент globals:
        Он содержит словарь, обеспечивающий доступ eval() к глобальному пространству имен.
        С помощью глобальных переменных можно указать eval(), какие глобальные имена использовать при выполнении выражения.
        Все имена, переданные глобальным переменным в словаре, будут доступны eval() во время выполнения.
        eval() имеет доступ к встроенным функциям.

        Примеры:
            eval("x + y", {"x": x})
            eval("x + y + z", {"x": x, "y": y, "z": 300})
    

"""
)
        case "5":
            timetype = input(symbolPrint("\nSYS> Что вы хотите установить?\n0. Выйти\n1. Секндомер\n2. Таймер\n\n> "))

            match timetype:
                case "0":
                    break
                case "1":
                    seconds,minutes,hours = 0,0,0
                    symbolPrint("\nSYS> Секндомер запущен! Нажмите 'q' для выхода.\n\n")
                    
                    while True: 
                        time.sleep(1)

                        if keyboard.is_pressed('q'):  # Выход при нажатии 'q'
                            symbolPrint("\n\nSYS> Секундомер остановлен.\n\n")
                            break
                        
                        if seconds == 60:
                            seconds = 0
                            minutes+=1
                        if minutes == 60:
                            minutes = 0
                            hours+=1

                        if hours > 0:
                            print(f"Время: {hours:02}:{minutes:02}:{seconds:02}",sep='',end='\r')   
                        elif minutes > 0:
                            print(f"Время: {minutes:02}:{seconds:02}",sep='',end='\r')
                        else: 
                            print(f"Время: {seconds:02}",sep='',end='\r')

                        seconds+=1
                case "2":
                    timertext = input(symbolPrint("\nSYS> О чём вам напомнить?\n\n> "))
                    timerhour, timermin, timersek = map(int, input(symbolPrint("\nSYS> На сколько времени (h:m:s)?\n\n> ")).split(":"))

                    if timersek > 60:
                        timersek -= 60
                        timermin += 1
                    if timermin > 60:
                        timermin -= 60
                        timerhour += 1

                    print()
                    while timerhour >= 0 and timermin >= 0 and timersek >= 0:
                        time.sleep(0.1)

                        if keyboard.is_pressed('q'):  # Выход при нажатии 'q'
                            symbolPrint("\n\nSYS> Секндомер остановлен.\n\n")
                            break
                        
                        if timerhour > 0:
                            if timermin == 0:
                                timerhour -= 1
                                timermin = 60
                        if timermin > 0:
                            if timersek == 0:
                                timermin -= 1
                                timersek = 60

                        print(f"Время: {timerhour:02}:{timermin:02}:{timersek:02}",sep='',end='\r')  
                        timersek -= 1
                    symbolPrint(f"\nНапоминание: {timertext}\n\n")
                        
        case "clear":
            clear = lambda: os.system('cls')
            clear()
        case _:
            symbolPrint(sys_err + "\n\n")