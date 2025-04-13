import csv
import psycopg2

conn = psycopg2.connect(host="localhost", dbname="lab10", user="postgres", password="Almaty250505", port=5432)
cur = conn.cursor()

# Кестені алу
cur.execute("SELECT * from phonebook;")
rows = cur.fetchall()

# CSV файлына жазу
with open('student.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Surname", "Phone"])  # Бағандардың аттарын жазу
    writer.writerows(rows)  # Кестенің мәліметтерін жазу

conn.commit()
cur.close()
conn.close()

print("Деректер студент.csv файлына сақталды.")
