import time, sqlite3
from parameters import params

def param(name):
    for keys, value in params.items():
        if name in keys:
            return value
    symbolPrint("Папка не найдена")
    return

def symbolPrint(str):
    for i in str:
        print(i, end="", flush=True)
        time.sleep(0.062)
    return ""

conn = sqlite3.connect(f"{param("path")}/module/apis.db")
cursor = conn.cursor()

def get_api_by_id():
    cursor.execute("SELECT api, apic, apicur FROM apis WHERE id = ?", (param("my_id"),))
    result = cursor.fetchone()
    
    if result:
        api, apic, apicur = result
        return api, apic, apicur
    else:
        return "\nSYS> Пользователь с таким ID не найден."