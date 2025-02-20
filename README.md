# SYS-Assistant

## Инструкция
Рекомендую сделать ярлык файла `assistant.py`
Сделать его можно при помощи создания ярлыка с расположением: 
`C:\Users\[Имя пользователя]\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe "Путь к файлу assistant.py"` для тех кто установил python с Microsoft Store
`python.exe "Путь к файлу assistant.py"` для тех кто установил python не с Microsoft Store

Чтобы терминал не закрывался зайдите в **Терминал > Параметры > По умолчанию > Расширения > Действия закрытия профиля и выберите 'Никогда не закрывать автоматически'**

В `calc.py` и там укажите путь к папке `SYS-Assistant`

## Добавление данных
При открытии он спрашивает ID из базы данных, чтобы ее создать нужно запустить файл `create and add to db.py` и ввести Номер ID, Имя, API с сайта [openweathermap](https://home.openweathermap.org/api_keys), API с сайта [cohere](https://dashboard.cohere.com/api-keys)
В `calc.py` и `minidefs.py` введите путь до **SYS-Assistant**

Чтобы добавить свое приложение в **SYS-Assistant** зайдите в `applications.py` и в словаре введите название по которому будет запускаться приложение а дальше введите путь к файлу.
**Обязательно: уберите двойные ковычки и используйтие / вместо \ Если несколько слов для запуска одного приложения введите () как в других.**

На данный момент всё.
**Дальше -- Больше**
