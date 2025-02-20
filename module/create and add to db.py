import sqlite3

conn = sqlite3.connect("C:/[Путь к SYS-Assistant]/SYS-Assistant/module/apis.db")
cursor = conn.cursor()
id, name, apiw, apic = map(str, input().split())

cursor.execute("""
CREATE TABLE IF NOT EXISTS apis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    api TEXT NOT NULL,
    apic TEXT NOT NULL
)
""")

cursor.execute("INSERT INTO apis (id, name, api, apic) VALUES (?, ?, ?, ?)", (id, name, apiw, apic))

conn.commit()
conn.close()

print("Данные успешно добавлено в базу данных!")