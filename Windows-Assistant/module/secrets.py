import secrets, string
from minidefs import symbolPrint

def secret():
    type = input(symbolPrint("\nSYS> Что вы хотите сгенерировать?\n1. Пароль\n2. Токен байтовый\n3. Токен hex\n4. Случайное число\n5. Случайный идентификатор\n6. Рандомные биты\n\n> "))

    match type:
        case "1":
            leng = input(symbolPrint("\nSYS> Какой длинны хотите сгенерировать пароль?\n\n> "))

            alphabet = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(alphabet) for _ in range(int(leng)))
            symbolPrint(password + "\n\n")
        case "2":
            byte = input(symbolPrint("\nSYS> Сколько байт хотите сгенерировать>\n\n> "))

            token = secrets.token_bytes(byte)
            symbolPrint(token + "\n\n")
        case "3":
            byte = input(symbolPrint("\nSYS> Сколько байт хотите сгенерировать>\n\n> "))

            hex_token = secrets.token_hex(16)
            symbolPrint(hex_token + "\n\n")
        case "4":
            leng = input(symbolPrint("\nSYS> Какой длинны хотите сгенерировать число?\n\n> "))

            random_number = secrets.randbelow(leng)
            symbolPrint(random_number + "\n\n")
        case "5":
            leng = input(symbolPrint("\nSYS> Какой длинны хотите сгенерировать идентификатор/url?\n\n> "))

            urlsafe_token = secrets.token_urlsafe(leng)
            symbolPrint(urlsafe_token+ "\n\n")
        case "6":
            bit = input(symbolPrint("\nSYS> Сколько создать бит?\n\n> "))

            random_bits = secrets.randbits(bit)
            symbolPrint(bit)