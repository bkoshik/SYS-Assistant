import time, webbrowser, os, sqlite3, math # Для 4 варианта
from calc import calc
from minidefs import symbolPrint, get_api_by_id
from timer import  timer
from weather import weather
from datetime import datetime
from deep_translator import GoogleTranslator
date = datetime.now()
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))

print("\033[38;2;0;180;0m", end="")

conn = sqlite3.connect("C:/Users/kudai/Рабочий стол/Github/SYS-Assistant/weather.db")
cursor = conn.cursor()

user_id = input(symbolPrint("SYS> Введите свой id из базы данных\n\n> "))

user_id = int(user_id)
api = get_api_by_id(user_id)
print()

sys_ques = """SYS> Введите:
0. Выйти
1. Узнать дату и время
2. Узнать погоду
3. Открыть веб-сайт
4. Ввести python-команды
5. Секундомер/Таймер
6. Калькулятор
7. Переводчик

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
                    url = input(symbolPrint("\nSYS> Что вы хотите найти\n\n> "))
                    webbrowser.get('Chrome').open_new_tab('https://www.google.com/search?q={}'.format(url))
                    print()
        case "4" | "py" | "python" | "command":
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
                            print()
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
        case "5" | "timer":
            timer()
        case "6" | "calc" | "calculator":
            calc()
        case "7" | "translator" | "translate":
            lang_from = input(symbolPrint("\nSYS> С какого языка вы хотите перевести?\n\n> "))
            lang_to = input(symbolPrint("\nSYS> На какой язык нужно перевести?\n\n> "))
            text = input(symbolPrint("\nSYS> Введите текст который нужно перевести\n\n> "))
            translator = GoogleTranslator(source=lang_from, target=lang_to)
            translated = translator.translate(text)
            symbolPrint("\nSYS> Перевод: \n" + translated + "\n\n")
        case "clear":
            clear = lambda: os.system('cls')
            clear()
        case _:
            symbolPrint(sys_err + "\n\n")