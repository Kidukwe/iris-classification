import pandas as pd
import sqlite3

# читаем CSV
df = pd.read_csv("iris_data.csv")

# создаём/открываем базу SQLite
conn = sqlite3.connect("iris_data.db")

# записываем данные в таблицу iris_data
df.to_sql("iris_data", conn, if_exists="replace", index=False)
conn.close()
print("iris_data.db успешно создан и заполнен")