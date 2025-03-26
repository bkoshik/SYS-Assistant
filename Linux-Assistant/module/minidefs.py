import time, sqlite3
from parameter import params

def param(name):
    for keys, value in params.items():
        if name in keys:
            return value
    symbolPrint("Папка не найдена")
    return

def symbolPrint(str):
    for i in str:
        print(i, end="", flush=True)
        time.sleep(0.05)
    return ""

conn = sqlite3.connect(f"{param("path")}/module/apis.db")
cursor = conn.cursor()
