import sqlite3

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()
id, name, api = map(str, input().split())

cursor.execute("INSERT INTO api (id, name, api) VALUES (?, ?, ?)", (id, name, api))

conn.commit()
conn.close()

print("Данные успешно добавлено в базу данных!")