#!/bin/bash

read -p "Введите массу (в кг): " weight
read -p "Введите рост (в метрах): " height

# Замена запятой на точку
height="${height//,/.}"
weight="${weight//,/.}"

# Вычисление целого значения ИМТ
bmi=$(echo "$weight / ($height * $height)" | bc)

echo "Индекс массы тела: $bmi"
