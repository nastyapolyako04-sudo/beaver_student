-- 1. Записи, где цена в диапазоне от 1000 до 50000 включительно
SELECT * FROM prices 
WHERE price BETWEEN 1000 AND 50000;

-- 2. Цена от 500 до 70000 и product_id <= 5
SELECT * FROM prices 
WHERE price BETWEEN 500 AND 70000 
  AND product_id <= 5;

-- 3. Цена меньше 100 или в диапазоне от 60000 до 70000
SELECT * FROM prices 
WHERE price < 100 
   OR price BETWEEN 60000 AND 70000;
