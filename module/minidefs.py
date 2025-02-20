import time, sqlite3

conn = sqlite3.connect("C:/[Путь до ассистента]/SYS-Assistant/module/apis.db")
cursor = conn.cursor()

def symbolPrint(str):
    for i in str:
        print(i, end="", flush=True)
        time.sleep(0.062)
    return ""

def get_api_by_id(user_id):
    cursor.execute("SELECT api, apic, apicur FROM apis WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    
    if result:
        api, apic, apicur = result
        return api, apic, apicur
    else:
        return "\nSYS> Пользователь с таким ID не найден."

