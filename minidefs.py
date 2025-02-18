import time, sqlite3

conn = sqlite3.connect("C:/Users/kudai/Рабочий стол/Github/SYS-Assistant/weather.db")
cursor = conn.cursor()

def symbolPrint(str):
    for i in str:
        print(i, end="", flush=True)
        # time.sleep(0.08)
    return ""

def get_api_by_id(user_id):
    cursor.execute("SELECT api FROM weather WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    
    if result:
        return result[0]  # Возвращаем имя
    else:
        return "Пользователь с таким ID не найден."