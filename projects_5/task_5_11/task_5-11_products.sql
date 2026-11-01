-- 1. Товары из категории «Электроника»
SELECT * FROM products 
WHERE category = 'Электроника';

-- 2. Товары категории «Одежда», у которых в названии есть «женские»
SELECT * FROM products 
WHERE category = 'Одежда' AND name ILIKE '%женские%';

-- 3. Товары, которые относятся к категории «Продукты» или «Книги»
SELECT * FROM products 
WHERE category IN ('Продукты', 'Книги');

-- 4. Все товары, не относящиеся к категории «Бытовая техника»
SELECT * FROM products 
WHERE category != 'Бытовая техника';

-- 5. Товары из категорий «Электроника», «Одежда» или «Книги»
SELECT * FROM products 
WHERE category IN ('Электроника', 'Одежда', 'Книги');

-- 6. Электроника с «Samsung» в названии ИЛИ бытовая техника
SELECT * FROM products 
WHERE (category = 'Электроника' AND name ILIKE '%Samsung%') 
   OR category = 'Бытовая техника';

-- 7. (Электроника, одежда или бытовая техника С id от 1 до 15 И БЕЗ «Samsung») ИЛИ книги
SELECT * FROM products 
WHERE (category IN ('Электроника', 'Одежда', 'Бытовая техника') 
       AND id BETWEEN 1 AND 15 
       AND name NOT ILIKE '%Samsung%') 
   OR category = 'Книги';
