import webbrowser, os, math # Для 4 варианта
from module.calc import calc
from module.minidefs import symbolPrint, get_api_by_id
from module.timersek import  timer
from module.weather import weather
from module.commands import commands
from module.applications import apps
from module.cohere import gpt
from datetime import datetime
from deep_translator import GoogleTranslator

date = datetime.now()
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))

print("\033[38;2;0;180;0m", end="")

while True:
    user_id = input(symbolPrint("SYS> Введите свой ID из базы данных\n\n> "))

    try:
        user_id = int(user_id)
        api, apic = get_api_by_id(user_id)
        
        if api is None or apic is None:
            symbolPrint("\nSYS> Пользователь с таким ID не найден.\n\n")
        else:
            break
        
    except ValueError:
        symbolPrint("\nSYS> Введите корректный числовой ID.\n\n")

clear = lambda: os.system('cls')
clear()

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

"""
sys = "SYS> Что вы хотите сделать?\n\n"
sys_err = "\nSYS> Пожалуйста, уточните ваш запрос."
inputChar = "> "

symbolPrint(sys_ques)

while True:
    symbolPrint(sys)

    sys_input = input(inputChar)

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
            weather(api)
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
            calc()
        case "7" | "translator" | "translate":
            try:
                lang_from = input("\nSYS> С какого языка вы хотите перевести?\n\n> ").strip()
                lang_to = input("\nSYS> На какой язык нужно перевести?\n\n> ").strip()
                text = input("\nSYS> Введите текст который нужно перевести\n\n> ").strip()

                if not lang_from or not lang_to or not text:
                    raise ValueError("Все поля должны быть заполнены!")

                translator = GoogleTranslator(source=lang_from, target=lang_to)
                translated = translator.translate(text)

                print("\nSYS> Перевод: \n" + translated + "\n\n")

            except ValueError as e:
                print(f"\nSYS> Ошибка: {e}\n")

            except Exception as e:
                print(f"\nSYS> Произошла ошибка: {e}\n")
        case "8" | "programm" | "app":
            def find_app(name):
                for keys, value in apps.items():
                    if name in keys:
                        return value
                return "Приложение не найдено"
            app = input(symbolPrint('\nSYS> Введите название программы или путь к программе в "ковычках"\n\n> '))

            if app.replace("/", r"\\").startswith('"C:\\'):
                os.startfile(app)
            else:
                os.startfile(find_app(app))
            print()
        case "9" | 'ai':
            gpt(apic)
        case "clear":
            clear()
        case _:
            symbolPrint(sys_err + "\n\n")