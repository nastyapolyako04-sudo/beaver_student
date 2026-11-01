import psycopg2

try:
    # Подключение к СУБД PostgreSQL в Docker
    connection = psycopg2.connect(
        host="localhost",
        port=5435,
        database="student_task",
        user="postgres",
        password="student"
    )

    cursor = connection.cursor()

    # Выполнение SQL-запроса
    cursor.execute("SELECT id, name, category FROM products LIMIT 5;")
    rows = cursor.fetchall()

    print("Результат выполнения запроса:")
    for row in rows:
        print(f"ID: {row[0]} | Товар: {row[1]} | Категория: {row[2]}")

    cursor.close()
    connection.close()
    print("\nПодключение успешно завершено и закрыто.")

except Exception as error:
    print(f"Ошибка при работе с PostgreSQL: {error}")
