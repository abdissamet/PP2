import psycopg2
import csv

# Дерекқор параметрлері
DB_NAME = "lab10"
DB_USER = "postgres"
DB_PASSWORD = "Almaty250505"
DB_HOST = "localhost"
DB_PORT = "5432"

# Дерекқорға қосылу
def connect_db():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()
    return conn, cur

# Phonebook кестесін құру
def create_phonebook_table():
    conn, cur = connect_db()
    cur.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_schema = 'public' 
              AND table_name = 'phonebook'
        );
    """)
    exists = cur.fetchone()[0]
    if exists:
        print("Таблица phonebook уже существует.")
    else:
        cur.execute('''
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                phone VARCHAR(255) NOT NULL
            )
        ''')
        conn.commit()
        print("Таблица phonebook создана.")
    cur.close()
    conn.close()

# Консоль арқылы дерек енгізу
def insert_data_from_console():
    conn, cur = connect_db()
    cur.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_schema = 'public' 
              AND table_name = 'phonebook'
        );
    """)
    exists = cur.fetchone()[0]
    if exists:
        try:
            count = int(input("Сколько записей хотите добавить: "))
        except ValueError:
            print("Некорректное число.")
            cur.close()
            conn.close()
            return
        for i in range(count):
            username = input(f"Введите имя пользователя {i+1}: ")
            while True:
                phone = input(f"Введите номер телефона {i+1}: ")
                if phone and (phone[0] == '+' or phone[0] == '8'):
                    break
                else:
                    print("Введите правильный номер для записи", i+1)
            # Егер қолданушы бар болса, жаңартылады, әйтпесе жаңасы қосылады
            cur.execute("SELECT id FROM phonebook WHERE username = %s", (username,))
            row = cur.fetchone()
            if row:
                cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (phone, username))
                print("Номер телефона обновлен.")
            else:
                cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
                print("Данные добавлены.")
        conn.commit()
        cur.close()
        conn.close()
    else:
        print("Создайте таблицу phonebook.")

# Жазбаларды pagination арқылы шығару
def query_phonebook_pagination():
    conn, cur = connect_db()
    cur.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_schema = 'public' 
              AND table_name = 'phonebook'
        );
    """)
    exists = cur.fetchone()[0]
    if not exists:
        print("Таблица phonebook не существует. Создайте таблицу.")
        cur.close()
        conn.close()
        return
    cur.execute("SELECT COUNT(*) FROM phonebook;")
    total_records = cur.fetchone()[0]
    print(f"Всего записей: {total_records}")
    while True:
        try:
            limit = int(input("Введите количество записей (limit): "))
            offset = int(input("Введите смещение (offset): "))
            if limit < 1:
                print("Limit должен быть больше 0. Введите правильное число.")
            elif offset < 0:
                print("Offset не может быть отрицательным. Введите правильное число.")
            elif offset >= total_records:
                print(f"Offset ({offset}) больше или равен общему количеству записей ({total_records}). Введите правильное число.")
            elif offset + limit > total_records:
                print(f"Записей недостаточно: offset + limit = {offset + limit}, а всего записей {total_records}. Введите правильные значения.")
            else:
                break
        except ValueError:
            print("Введите корректное целое число.")
    cur.execute("""
        SELECT id, username, phone
        FROM phonebook
        ORDER BY id
        LIMIT %s OFFSET %s;
    """, (limit, offset))
    rows = cur.fetchall()
    print("\nРезультаты запроса:")
    if rows:
        for row in rows:
            print(row)
    else:
        print("Нет записей.")
    cur.close()
    conn.close()

# CSV файлдан жазбалар қосу
def insert_data_from_csv(csv_file):
    conn, cur = connect_db()
    cur.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_schema = 'public' 
              AND table_name = 'phonebook'
        );
    """)
    exists = cur.fetchone()[0]
    if exists:
        try:
            with open(csv_file, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 2:
                        continue
                    username, phone = row[0], row[1]
                    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
            conn.commit()
            print("Данные из CSV добавлены.")
        except FileNotFoundError:
            print("Файл не найден.")
        cur.close()
        conn.close()
    else:
        print("Создайте таблицу phonebook.")

# Аты немесе телефоны бойынша жазбаны жаңарту
def update_phonebook():
    conn, cur = connect_db()
    cur.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_schema = 'public' 
              AND table_name = 'phonebook'
        );
    """)
    exists = cur.fetchone()[0]
    if exists:
        mode = input("Что хотите изменить? (1) Имя, (2) Телефон: ")
        if mode == "1":
            old_name = input("Текущее имя: ")
            new_name = input("Новое имя: ")
            cur.execute("UPDATE phonebook SET username=%s WHERE username=%s", (new_name, old_name))
            if cur.rowcount > 0:
                print("Имя обновлено.")
            else:
                print("Имя не найдено.")
        elif mode == "2":
            user_name = input("Имя пользователя: ")
            new_phone = input("Новый телефон: ")
            cur.execute("UPDATE phonebook SET phone=%s WHERE username=%s", (new_phone, user_name))
            if cur.rowcount > 0:
                print("Телефон обновлен.")
            else:
                print("Пользователь не найден.")
        else:
            print("Некорректный выбор.")
        conn.commit()
        cur.close()
        conn.close()
    else:
        print("Создайте таблицу phonebook.")

# Кестеден жазбаларды сұрау
def query_phonebook():
    conn, cur = connect_db()
    cur.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_schema = 'public' 
              AND table_name = 'phonebook'
        );
    """)
    exists = cur.fetchone()[0]
    if exists:
        mode = input("Фильтр? (1) Нет, (2) По имени, (3) По телефону: ")
        if mode == "1":
            cur.execute("SELECT id, username, phone FROM phonebook ORDER BY id;")
        elif mode == "2":
            pattern = input("Часть имени: ")
            cur.execute("SELECT id, username, phone FROM phonebook WHERE username ILIKE %s ORDER BY id;", (f"%{pattern}%",))
        elif mode == "3":
            pattern = input("Часть телефона: ")
            cur.execute("SELECT id, username, phone FROM phonebook WHERE phone ILIKE %s ORDER BY id;", (f"%{pattern}%",))
        else:
            print("Некорректный выбор. Покажем все записи.")
            cur.execute("SELECT id, username, phone FROM phonebook ORDER BY id;")
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("Нет записей.")
        cur.close()
        conn.close()
    else:
        print("Создайте таблицу phonebook.")

# Жазбаларды жою (аты немесе телефоны бойынша)
def delete_data():
    conn, cur = connect_db()
    cur.execute("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_schema = 'public' 
              AND table_name = 'phonebook'
        );
    """)
    exists = cur.fetchone()[0]
    if exists:
        mode = input("Удалить по (1) имени или (2) телефону? ")
        if mode == "1":
            name = input("Введите имя: ")
            cur.execute("DELETE FROM phonebook WHERE username=%s", (name,))
        elif mode == "2":
            phone = input("Введите телефон: ")
            cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))
        else:
            print("Некорректный выбор.")
            cur.close()
            conn.close()
            return
        if cur.rowcount > 0:
            print("Запись(и) удалены.")
        else:
            print("Ничего не удалено.")
        conn.commit()
        cur.close()
        conn.close()
    else:
        print("Создайте таблицу phonebook.")

# Кестені толығымен жою
def delete_table():
    conn, cur = connect_db()
    mode = input("Вы точно хотите удалить таблицу? Да(1) / Нет(2): ")
    if mode == "1":
        cur.execute("DROP TABLE IF EXISTS phonebook CASCADE;")
        conn.commit()
        print("Таблица phonebook успешно удалена.")
    else:
        print("Удаление отменено.")
    cur.close()
    conn.close()


# Негізгі мәзір — қолданушыға барлық функцияларға қол жеткізу мүмкіндігі
def main_menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Создать таблицу")
        print("2. Добавить запись (консоль)")
        print("3. Добавить записи из CSV")
        print("4. Обновить запись (имя или телефон)")
        print("5. Показать записи")
        print("6. Удалить запись")
        print("7. Удалить таблицу")
        print("8. Выборный вывод")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            create_phonebook_table()
        elif choice == "2":
            insert_data_from_console()
        elif choice == "3":
            csv_file = input("Имя CSV-файла: ")
            insert_data_from_csv(csv_file)
        elif choice == "4":
            update_phonebook()
        elif choice == "5":
            query_phonebook()
        elif choice == "6":
            delete_data()
        elif choice == "7":
            delete_table()
        elif choice == "0":
            print("Выход.")
            break
        elif choice == "8":
            query_phonebook_pagination()
        else:
            print("Некорректный выбор.")

# Бағдарлама іске қосылғанда негізгі мәзір басталады
if __name__ == "__main__":
    main_menu()