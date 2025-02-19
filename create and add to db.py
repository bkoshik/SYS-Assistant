import sqlite3

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()
id, name, api = map(str, input().split())

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    api TEXT NOT NULL
)
""")

cursor.execute("INSERT INTO weather (id, name, api) VALUES (?, ?, ?)", (id, name, api))

conn.commit()
conn.close()

print("Данные успешно добавлено в базу данных!")