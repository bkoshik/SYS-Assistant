from math import *
from minidefs import symbolPrint, param
from datetime import datetime
import os, requests

def calc(apicur):
    calccur = input(symbolPrint("\nSYS> Калькулятор или конвертер валют?\n0. Выйти\n1. Конвертер валют\n2. Калькулятор\n\n> "))

    match calccur:
        case "0":
            return
        case "1":
            BASE_URL = f"https://v6.exchangerate-api.com/v6/{apicur}/latest/"

            def convert_currency(amount, from_currency, to_currency):
                response = requests.get(BASE_URL + from_currency)
                data = response.json()

                if response.status_code != 200 or "conversion_rates" not in data:
                    return "\nSYS> Ошибка получения курса валют\n\n"

                rate = data["conversion_rates"].get(to_currency)
                if rate is None:
                    return "\nSYS> Валюта не найдена\n\n"

                return f"{amount} {from_currency} = {amount * rate:.2f} {to_currency}"

            amount = float(input(symbolPrint("\nSYS> Введите сумму\n\n> ")))
            from_currency = input(symbolPrint("\nSYS> Из какой валюты\n\n> ")).upper()
            to_currency = input(symbolPrint("\nSYS> В какую валюту\n\n> ")).upper()

            symbolPrint("\nSYS> " + str(convert_currency(amount, from_currency, to_currency)) + "\n\n")
        case "2":
            date = datetime.now()
            hfile = f"{param("path")}/module/calc history.txt"

            if not os.path.exists(hfile):
                open(hfile, "w").close()

            con = "1"

            quescon = input(symbolPrint("\nSYS> Спрашивать каждый раз 'продолжить'?\n0. Выйти\n1. Да\n2. Нет\n\n> ")).strip()
            if quescon == "0" or quescon == "exit":
                return
            
            symbolPrint("\nSYS> Чтобы выйти введите 'END' или 'exit' в операции\n")
            while con == "1":
                op = input(symbolPrint("\nSYS> Введите операцию:\n+, -, *, /, ^, sqr, fact, gcd, lcm\nsqsum, sqdif\n\n> ")).strip()

                if op == "sqr" or op == "fact":
                    num1 = float(input(symbolPrint("\nSYS> Введите первое число\n\n> ")).strip())
                elif op == "history":
                    None
                else:
                    num1 = float(input(symbolPrint("\nSYS> Введите первое число\n\n> ")).strip())
                    num2 = float(input(symbolPrint("\nSYS> Введите второе число\n\n> ")).strip())

                match op:
                    case "+":
                        symbolPrint("\nSYS> Сумма:\n" + str(num1 + num2))
                        hresult = f"{num1} + {num2} = {num1+num2}"
                    case "-":
                        symbolPrint("\nSYS> Разность:\n" + str(num1 - num2))
                        hresult = f"{num1} - {num2} = {num1-num2}"
                    case "*":
                        symbolPrint("\nSYS> Произведение:\n" + str(num1 * num2))
                        hresult = f"{num1} * {num2} = {num1*num2}"
                    case "/":
                        if num2 == 0:
                            symbolPrint("\nSYS> Деление на ноль\n")
                            continue
                        else:
                            symbolPrint("\nSYS> Частное:\n" + str(num1 / num2))
                            hresult = f"{num1} / {num2} = {num1/num2}"
                    case "^":
                        symbolPrint("\nSYS> Степень:\n" + str(pow(num1, num2)))
                        hresult = f"{num1} ^ {num2} = {pow(num1, num2)}"
                    case "sqr":
                        symbolPrint("\nSYS> Квадратный корень:\n" + str(sqrt(num1)))
                        hresult = f"√{num1} = {sqrt(num1)}"
                    case "fact":
                        symbolPrint("\nSYS> Факториал:\n" + str(factorial(int(num1))))
                        hresult = f"{num1}! = {factorial(num1)}"
                    case "gcd":
                        symbolPrint("\nSYS> НОД:\n" + str(gcd(int(num1), int(num2))))
                        hresult = f"GCD: {num1}, {num2} = {gcd(int(num1), int(num2))}"
                    case "lcm":
                        symbolPrint("\nSYS> НОК:\n" + str(lcm(int(num1), int(num2))))
                        hresult = f"LCM: {num1}, {num2} = {lcm(int(num1), int(num2))}"
                    case "sqsum":
                        symbolPrint("\nSYS> Квадрат суммы:\n" + str(num1**2 + 2*num1*num2 + num2**2))
                        hresult = f"{num1}^2 + 2*{num1}*{num2} + 2^{num2} = {num1**2 + 2*num1*num2 + num2**2}"
                    case "sqdif":
                        symbolPrint("\nSYS> Квадрат разности:\n" + str(num1**2 - 2*num1*num2 + num2**2))
                        hresult = f"{num1}^2 - 2*{num1}*{num2} + 2^{num2} = {num1**2 - 2*num1*num2 + num2**2}"
                    case "history" | "hst":
                        with open(hfile, "r") as file:
                            history = file.read()
                        symbolPrint("\n" + history if history else "\nSYS> История пуста")
                    case "END" | "exit":
                        return
                    case _:
                        symbolPrint("\nSYS> Введите правильную операцию")
                        continue
                
                if op != "history" or op != "hst":
                    with open(hfile, "a") as file:
                        date_str = f"{date.day:02}.{date.month:02}.{date.year}"
                        new_entry = f"\t{hresult}\n"

                        if os.path.exists(hfile):
                            with open(hfile, "r", encoding="utf-8") as file:
                                lines = file.readlines()

                            for i, line in enumerate(lines):
                                if line.strip() == date_str + ":":
                                    lines.insert(i + 1, new_entry)
                                    break
                            else:
                                lines.append(f"{date_str}:\n{new_entry}")
                        else:
                            lines = [f"{date_str}:\n{new_entry}"]

                        with open(hfile, "w", encoding="utf-8") as file:
                            file.writelines(lines)
                
                if quescon == "1":
                    con = input("\nSYS> Продолжить?\n0. Выйти\n1. Да\n2. Нет\n\n> ")
                if con == "0" or con == "exit":
                    return