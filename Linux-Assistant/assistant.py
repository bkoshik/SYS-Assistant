import webbrowser, subprocess, os, math
from module.calc import calc
from module.minidefs import symbolPrint
from module.timersek import  timer
from module.weather import weather
from module.commands import commands
from module.secrets import secret
from datetime import datetime
from module.parameter import params
from deep_translator import GoogleTranslator

date = datetime.now()
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser("chrome"))

print("\033[38;2;0;180;0m", end="")

sys_ques = """SYS> Введите:
0. Выйти
1. Узнать дату и время
2. Узнать погоду
3. Открыть веб-сайт
4. Ввести python-команды
5. Секундомер/Таймер
6. Калькулятор
7. Переводчик
8. Открыть программу
9. Сгенерировать что-то случайное
10. Выполнить команду из консоли

"""
sys = "SYS> Что вы хотите сделать?\n\n"
sys_err = "\nSYS> Пожалуйста, уточните ваш запрос."
inputChar = "> "

symbolPrint(sys_ques)

while True:
    symbolPrint(sys)

    sys_input = input(inputChar).strip()

    match sys_input:
        case "0" | "exit":
            exit()
        case "1" | "time":
            symbolPrint(
f"""
SYS> Текущее время:
{date.hour:02}:{date.minute:02}
{date.day:02}.{date.month:02}.{date.year}

"""
)
        case "2" | "weather":
            weather(params["api_weather"])
        case "3" | "web-site" | "site":
            typeUrl = input(symbolPrint("\nSYS> Что вы хотите найти?\n0. Выйти\n1. Веб-сайт\n2. Найти в поисковике\n\n> "))
            
            match typeUrl:
                case "0":
                    break
                case "1":
                    url = input(symbolPrint("\nSYS> Введите URL веб-сайта\n\n> "))
                    webbrowser.get('Chrome').open_new_tab(url)
                    print()
                case "2":
                    url = input(symbolPrint("\nSYS> Что вы хотите найти?\n\n> "))
                    webbrowser.get('Chrome').open_new_tab('https://www.google.com/search?q={}'.format(url))
                    print()
        case "4" | "py" | "python" | "command":
            commands()
        case "5" | "timer":
            timer()
        case "6" | "calc" | "calculator":
            calc(params["api_cur"])
        case "7" | "translator" | "translate":
            try:
                lang_from = input(symbolPrint("\nSYS> С какого языка вы хотите перевести?\n\n> ")).strip()
                lang_to = input(symbolPrint("\nSYS> На какой язык нужно перевести?\n\n> ")).strip()
                text = input(symbolPrint("\nSYS> Введите текст который нужно перевести\n\n> ")).strip()

                if not lang_from or not lang_to or not text:
                    raise ValueError(symbolPrint("Все поля должны быть заполнены!"))

                translator = GoogleTranslator(source=lang_from, target=lang_to)
                translated = translator.translate(text)

                symbolPrint(("\nSYS> Перевод: \n" + translated + "\n\n"))

            except ValueError as e:
                symbolPrint((f"\nSYS> Ошибка: {e}\n"))

            except Exception as e:
                symbolPrint((f"\nSYS> Произошла ошибка: {e}\n"))
        case "8" | "programm" | "app":
            app = input(symbolPrint('\nSYS> Введите название программы\n\n> '))
            app = app.replace(" ", "-").lower()

            subprocess.run(app)
            print()
        case "9"| "generate":
            secret()
        case "10"| "console" | "konsole" | "cmd":
            symbolPrint("\nSYS> Введите команду, чтобы выйти введите END")

            while True:
                usercmd = input(symbolPrint("\n\n> "))

                if usercmd == "END":
                    print()
                    break
                elif usercmd == "sys-as":
                    symbolPrint("\nSYS> Запустить эту программу из программы нельзя!")
                    continue

                cmd = lambda: os.system(usercmd)
                cmd()
        case "clear":
            clear = lambda: os.system('clear')
            clear()
        case _:
            symbolPrint(sys_err + "\n\n")
