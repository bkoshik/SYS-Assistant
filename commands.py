from minidefs import symbolPrint

def commands():
    startCom = input(symbolPrint("\nSYS> Хотите начать? (для завершения вводите END)\n0. Выйти\n1. Начать однострочное\n2. Начать многострочное\n3. Пройти обучение\n\n> "))

    match startCom:
        case "0":
            return
        case "1":
            while True:
                try:
                    lineOneCode = input(symbolPrint("\n>>> "))
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
                lineManyCode = input(symbolPrint(">>> "))
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