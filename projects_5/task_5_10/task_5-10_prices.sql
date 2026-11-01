-- 1. Выведите 5 самых дорогих записей из таблицы prices
SELECT * FROM prices ORDER BY price DESC LIMIT 5;

-- 2. Выведите 10 последних добавленных записей из таблицы prices, отсортированных по полю created_at
SELECT * FROM prices ORDER BY created_at DESC LIMIT 10;

-- 3. Выведите 10 самых дешёвых цен из таблицы prices
SELECT * FROM prices ORDER BY price ASC LIMIT 10;

-- 4. Выведите записи из таблицы prices: пропустите первые 20 самых дорогих значений и отобразите следующие
SELECT * FROM prices ORDER BY price DESC OFFSET 20;
