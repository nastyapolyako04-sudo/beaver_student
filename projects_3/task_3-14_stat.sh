#!/bin/bash

# 1. Сумма всех оценок
awk '{sum += $2} END {print sum}' students.txt

# 2. Средняя оценка
awk '{sum += $2} END {print sum / NR}' students.txt

# 3. Максимальная оценка
awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt
