from minidefs import symbolPrint
import cohere

def gpt(apic):
    co = cohere.Client(apic)

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