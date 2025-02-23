import keyboard,time
from minidefs import symbolPrint

def timer():
    timetype = input(symbolPrint("\nSYS> Что вы хотите установить?\n0. Выйти\n1. Секндомер\n2. Таймер\n\n> "))

    match timetype:
        case "0":
            return
        case "1":
            seconds,minutes,hours = 0,0,0
            symbolPrint("\nSYS> Секндомер запущен! Нажмите 'q' для выхода.\n\n")
            
            while True: 
                time.sleep(1)

                if keyboard.is_pressed('q'):
                    symbolPrint("\n\nSYS> Секундомер остановлен.\n\n")
                    break
                
                if seconds == 60:
                    seconds = 0
                    minutes+=1
                if minutes == 60:
                    minutes = 0
                    hours+=1

                if hours > 0:
                    print(f"Время: {hours:02}:{minutes:02}:{seconds:02}",sep='',end='\r')   
                elif minutes > 0:
                    print(f"Время: {minutes:02}:{seconds:02}",sep='',end='\r')
                else: 
                    print(f"Время: {seconds:02}",sep='',end='\r')

                seconds+=1
        case "2":
            timertext = input(symbolPrint("\nSYS> О чём вам напомнить?\n\n> "))
            timerhour, timermin, timersek = map(int, input(symbolPrint("\nSYS> На сколько времени (h:m:s)?\n\n> ")).split(":"))

            if timersek > 60:
                timersek -= 60
                timermin += 1
            if timermin > 60:
                timermin -= 60
                timerhour += 1

            print()
            while timerhour >= 0 and timermin >= 0 and timersek >= 0:
                time.sleep(0.1)

                if keyboard.is_pressed('q'):  # Выход при нажатии 'q'
                    symbolPrint("\n\nSYS> Секндомер остановлен.\n\n")
                    break
                
                if timerhour > 0:
                    if timermin == 0:
                        timerhour -= 1
                        timermin = 60
                if timermin > 0:
                    if timersek == 0:
                        timermin -= 1
                        timersek = 60

                print(f"Время: {timerhour:02}:{timermin:02}:{timersek:02}",sep='',end='\r')  
                timersek -= 1
            symbolPrint(f"\nНапоминание: {timertext}\n\n")