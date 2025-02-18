from math import *

def calc():
    shure = "n"
    con = "y"
    num1 = 0

    while shure == "n":
        num1word = "Введите первое число: "
        num2word = "Введите второе число: "
        opword = "Введите операцию (+, -, *, /, ^, sqr, fact, gcd, lcm, sqsum, sqdif): "
        sumword = "Сумма: "
        diffword = "Разность: "
        prodword = "Произведение: "
        quotword = "Частное: "
        powword = "Степень: "
        sqrtword = "Квадратный корень: "
        factword = "Факториал: "
        gcdword = "НОД: "
        lcmword = "НОК: "
        sqsumword = "Квадрат суммы: "
        sqdifword = "Квадрат разности: "
        shureword = "Вы уверены? (y/n): "
        quesconword = "Спрашивать каждый раз продолжить (y/n): "
        conword = "Продолжить? (y/n): "
        zeroerror = "Ошибка: Деление на ноль"
        langerror = "Ошибка: Неверный язык"
        operror = "Ошибка: Введите правильную операцию"
        shure = input(shureword)
        quescon = input(quesconword)

    while con == "y":
        op = input(opword)
        if op == "sqr" or op == "fact":
            num1 = float(input(num1word))
        else:
            num1 = float(input(num1word))
            num2 = float(input(num2word))

        match op:
            case "+":
                print(sumword + str(num1 + num2))
            case "-":
                print(diffword + str(num1 - num2))
            case "*":
                print(prodword + str(num1 * num2))
            case "/":
                if num2 == 0:
                    print(zeroerror)
                    continue
                else:
                    print(quotword + str(num1 / num2))
            case "^":
                print(powword + str(pow(num1, num2)))
            case "sqr":
                print(sqrtword + str(sqrt(num1)))
            case "fact":
                print(factword + str(factorial(int(num1))))
            case "gcd":
                print(gcdword + str(gcd(int(num1), int(num2))))
            case "lcm":
                print(lcmword + str(lcm(int(num1), int(num2))))
            case "sqsum":
                print(sqsumword + str(num1**2 + 2*num1*num2 + num2**2))
            case "sqdif":
                print(sqdifword + str(num1**2 - 2*num1*num2 + num2**2))
            case _:
                print(operror)
                continue
        
        if quescon == "y":
            con = input(conword)