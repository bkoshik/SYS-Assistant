from math import *
from minidefs import symbolPrint

def calc():
    con = "1"

    quescon = input("\nSYS> Спрашивать каждый раз 'продолжить'?\n0. Выйти\n1. Да\n2. Нет\n\n> ")
    if quescon == "0" or quescon == "exit":
        return
    
    symbolPrint("\nSYS> Чтобы выйти введите 'END' или 'exit' в операции\n")
    while con == "1":
        op = input("\nSYS> Введите операцию\n+, -, *, /, ^, sqr, fact, gcd, lcm\nsqsum, sqdif\n\n> ")
        if op == "sqr" or op == "fact":
            num1 = float(input("\nSYS> Введите первое число\n\n> "))
        else:
            num1 = float(input("\nSYS> Введите первое число\n\n> "))
            num2 = float(input("\nSYS> Введите второе число\n\n> "))

        match op:
            case "+":
                print("\nSYS> Сумма:\n" + str(num1 + num2) + "\n")
            case "-":
                print("\nSYS> Разность:\n" + str(num1 - num2) + "\n")
            case "*":
                print("\nSYS> Произведение:\n" + str(num1 * num2))
            case "/":
                if num2 == 0:
                    print("\nSYS> Деление на ноль")
                    continue
                else:
                    print("\nSYS> Частное:\n" + str(num1 / num2) + "\n")
            case "^":
                print("\nSYS> Степень:\n" + str(pow(num1, num2)) + "\n")
            case "sqr":
                print("\nSYS> Квадратный корень:\n" + str(sqrt(num1)) + "\n")
            case "fact":
                print("\nSYS> Факториал:\n" + str(factorial(int(num1))) + "\n")
            case "gcd":
                print("\nSYS> НОД:\n" + str(gcd(int(num1), int(num2))) + "\n")
            case "lcm":
                print("\nSYS> НОК:\n" + str(lcm(int(num1), int(num2))) + "\n")
            case "sqsum":
                print("\nSYS> Квадрат суммы:\n" + str(num1**2 + 2*num1*num2 + num2**2) + "\n")
            case "sqdif":
                print("\nSYS> Квадрат разности:\n" + str(num1**2 - 2*num1*num2 + num2**2) + "\n")
            case "END" | "exit":
                return
            case _:
                print("\nSYS> Введите правильную операцию")
                continue
        
        if quescon == "1":
            con = input("\nSYS> Продолжить?\n0. Выйти\n1. Да\n2. Нет\n\n> ")
        if con == "0" or con == "exit":
            return