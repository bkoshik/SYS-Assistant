# SYS-Assistant

## Инструкция
### Windows:
  Рекомендую сделать ярлык файла `assistant.py`
  Сделать его можно при помощи создания ярлыка с расположением: 
  1. Python Microsoft Store: `C:\Users\[Имя пользователя]\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe "Путь к файлу assistant.py"`
  2. Python: `python.exe "Путь к файлу assistant.py"`
  
  Чтобы терминал не закрывался зайдите в **Терминал > Параметры > По умолчанию > Расширения > Действия закрытия профиля и выберите 'Никогда не закрывать автоматически'**

### Linux (на нём основная разработка):
  Чтобы установить введите:
  1. Zsh:
 
    git clone https://github.com/bkoshik/SYS-Assistant.git ~/.sys-assistant
    echo '
    
    sys-as() {
        source "$HOME/.sys-assistant/virtual-sys/bin/activate"
        python3 "$HOME/.sys-assistant/assistant.py"
        deactivate
    }' >> ~/.zshrc
    cd ~/.sys-assistant/
    source "$HOME/.sys-assistant/virtual-sys/bin/activate"
    pip install -r requirements.txt
    deactivate
    cd $HOME/

  2. Bash:

    git clone https://github.com/bkoshik/SYS-Assistant.git $HOME/.sys-assistant
    echo '
    
    sys-as() {
        source "$HOME/.sys-assistant/virtual-sys/bin/activate"
        python3 "$HOME/.sys-assistant/assistant.py"
        deactivate
    }' >> ~/.bashrc
    cd $HOME/.sys-assistant/
    source "$HOME/.sys-assistant/virtual-sys/bin/activate"
    pip install -r requirements.txt
    deactivate
    cd $HOME/

  3. Fish: Fish будет позже (я его не использую)

## Добавление данных
### Для Windows/Linux:
  В module/parameter.py уберите все '#' и замените "Введите ваш API ключ с ___" на ваш API ключ: 
  1. В 7 строке с сайта [OpenWeatherMap](https://home.openweathermap.org/api_keys)
  2. В 8 строке с сайта [ExchangeRate-API](https://app.exchangerate-api.com/dashboard)

### Windows:
  Чтобы добавить свое приложение в **SYS-Assistant** зайдите в `applications.py` и в словаре введите название по которому будет запускаться приложение а дальше введите путь к файлу.
  **Обязательно: уберите двойные ковычки и используйтие / вместо \ Если несколько слов для запуска одного приложения введите () как в других.**

На данный момент всё.

**Дальше -- Больше**
