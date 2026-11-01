-- Увеличьте цену на 10% для всех товаров, у которых текущая цена меньше 1000
UPDATE prices
SET price = ROUND(price * 1.10, 2)
WHERE price < 1000;
