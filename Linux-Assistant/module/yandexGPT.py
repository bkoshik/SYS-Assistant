from minidefs import symbolPrint
import requests

def gpt(apiai):
    symbolPrint("\nSYS> Введите свой запрос, чтобы выйти введите END")

    while True:
        userq = input(symbolPrint("\n\n> "))

        if userq == "END":
            break

        prompt = {
            "modelUri": "gpt://b1gb3qm552rgi7sbal0b/yandexgpt",
            "completionAsyncOptions": {
                "stream": False,
                "temperature": 0.2
            },
            "messages": [
                {
                    "role": "user",
                    "text": userq
                }
            ]
        }


        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Api-Key {apiai}"
        }

        text = requests.post(url, headers=headers, json=prompt).json()["result"]["alternatives"][0]["message"]["text"]

        symbolPrint("\nYandexGPT> " + text)
