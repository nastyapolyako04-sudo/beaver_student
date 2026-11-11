import psycopg2
import pandas as pd
import warnings

# Отключаем предупреждение pandas о работе напрямую через DBAPI2-соединение
warnings.filterwarnings('ignore', category=UserWarning)

try:
    # 1. Подключение к контейнеру PostgreSQL в Docker
    connection = psycopg2.connect(
        host="localhost",
        port=5435,
        database="student_task",
        user="postgres",
        password="student"
    )
    print("Соединение с PostgreSQL успешно установлено!\n")

    # 2. Выполнение SQL-запроса с JOIN и загрузка в pandas DataFrame
    query = """
    SELECT 
        p.name, 
        p.category, 
        pr.price 
    FROM prices pr
    JOIN products p ON pr.product_id = p.id;
    """
    df = pd.read_sql_query(query, connection)
    
    # Приводим столбец цен к вещественному типу данных
    df['price'] = pd.to_numeric(df['price'])

    # 3. Базовые статистические показатели по столбцу price
    mean_price = df['price'].mean()
    median_price = df['price'].median()
    std_price = df['price'].std()
    min_price = df['price'].min()
    max_price = df['price'].max()

    print("=== 3. Базовая статистика цен ===")
    print(f"Средняя цена:            {mean_price:.2f} руб.")
    print(f"Медиана:                 {median_price:.2f} руб.")
    print(f"Стандартное отклонение:  {std_price:.2f} руб.")
    print(f"Минимальная цена:        {min_price:.2f} руб.")
    print(f"Максимальная цена:       {max_price:.2f} руб.\n")

    # 4. Квартили, межквартильный размах (IQR) и товары дороже Q3
    q1 = df['price'].quantile(0.25)
    q2 = df['price'].quantile(0.50)  # Медиана
    q3 = df['price'].quantile(0.75)
    iqr = q3 - q1

    print("=== 4. Квартили и межквартильный размах ===")
    print(f"Первый квартиль (Q1):    {q1:.2f} руб.")
    print(f"Второй квартиль (Q2):    {q2:.2f} руб.")
    print(f"Третий квартиль (Q3):    {q3:.2f} руб.")
    print(f"Межквартильный размах:   {iqr:.2f} руб.\n")

    expensive_products = df[df['price'] > q3][['name', 'category', 'price']].drop_duplicates(subset=['name'])
    print(f"Товары с ценой выше Q3 ({q3:.2f} руб.):")
    for _, row in expensive_products.iterrows():
        print(f"- {row['name']} [{row['category']}]: {row['price']:.2f} руб.")
    print()

    # 5. Группировка по категориям
    print("=== 5. Статистика по категориям товаров ===")
    category_stats = df.groupby('category')['price'].agg(
        count='count',
        mean='mean',
        median='median',
        std='std'
    ).sort_values(by='mean', ascending=False)
    
    # Форматирование вывода таблицы категорий
    category_stats_formatted = category_stats.copy()
    category_stats_formatted['mean'] = category_stats_formatted['mean'].round(2).astype(str) + " руб."
    category_stats_formatted['median'] = category_stats_formatted['median'].round(2).astype(str) + " руб."
    category_stats_formatted['std'] = category_stats_formatted['std'].round(2).astype(str) + " руб."
    category_stats_formatted.columns = ['Кол-во записей', 'Средняя цена', 'Медиана', 'Станд. откл.']
    print(category_stats_formatted)
    print()

    # 6. Пять товаров с наибольшим разбросом цен
    print("=== 6. Топ-5 товаров с наибольшим разбросом цен ===")
    product_spread = df.groupby('name')['price'].agg(min_price='min', max_price='max').copy()
    product_spread['spread'] = product_spread['max_price'] - product_spread['min_price']
    top_5_spread = product_spread.sort_values(by='spread', ascending=False).head(5)

    for name, row in top_5_spread.iterrows():
        print(f"Товар: {name}")
        print(f"  Мин: {row['min_price']:.2f} руб. | Макс: {row['max_price']:.2f} руб. | Разброс: {row['spread']:.2f} руб.")

    # Закрытие соединения
    connection.close()
    print("\nРабота завершена, соединение с базой данных закрыто.")

except Exception as error:
    print(f"Произошла ошибка: {error}")
