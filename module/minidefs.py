import time, sqlite3

conn = sqlite3.connect("C:/Users/kudai/Рабочий стол/Github/SYS-Assistant/module/apis.db")
cursor = conn.cursor()

def symbolPrint(str):
    for i in str:
        print(i, end="", flush=True)
        time.sleep(0.062)
    return ""

def get_api_by_id(user_id):
    cursor.execute("SELECT api, apic FROM apis WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    
    if result:
        api, apic = result
        return api, apic
    else:
        return "\nSYS> Пользователь с таким ID не найден."

