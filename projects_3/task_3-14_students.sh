#!/bin/bash

# 1. Выведет только имена студентов
awk '{print $1}' students.txt

# 2. Выведет только оценки
awk '{print $2}' students.txt

# 3. Выведет номер строки и имя
awk '{print NR, $1}' students.txt
