#!/bin/bash

# Создаем 10 файлов
for i in {1..10}; do
    touch "test${i}.txt"
done

# Удаляем в обратном порядке
i=10
while [ $i -ge 1 ]; do
    rm "test${i}.txt"
    i=$((i - 1))
done
