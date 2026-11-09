#!/bin/bash

# 1. Выведет названия товаров
awk -F, '{print $2}' data.csv

# 2. Выведет товары дороже 20
awk -F, '$3 > 20' data.csv

# 3. Посчитает общую стоимость
awk -F, '{total += $3} END {print total}' data.csv
