from minidefs import symbolPrint
import cohere

def gpt():
    API_KEY = "Вставте свой API с https://dashboard.cohere.com/api-keys"
    co = cohere.Client(API_KEY)

    symbolPrint("\nSYS> Чтобы выйти, введите 'END'\n\nSYS> Введите свой запрос\n")

    while True:
        prompt = input(symbolPrint("\n> "))

        if prompt.strip().upper() == "END":
            symbolPrint("\nSYS> Завершение работы...\n")
            break

        response = co.generate(
            model='command',
            prompt=prompt
        )

        symbolPrint("\nSYS> Ответ:\n" + response.generations[0].text + "\n")