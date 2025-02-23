import sqlite3
from minidefs import symbolPrint, param

conn = sqlite3.connect(f"{param("path")}/module/apis.db")
cursor = conn.cursor()
id, name, apiw, apic, apicur = map(str, input().split())

cursor.execute("""
CREATE TABLE IF NOT EXISTS apis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    api TEXT NOT NULL,
    apic TEXT NOT NULL,
    apicur TEXT NOT NULL
)
""")

cursor.execute("INSERT INTO apis (id, name, api, apic, apicur) VALUES (?, ?, ?, ?, ?)", (id, name, apiw, apic, apicur))

conn.commit()
conn.close()

print("Данные успешно добавлено в базу данных!")