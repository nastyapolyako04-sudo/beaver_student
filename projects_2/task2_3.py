# --- Задание 1 ---
print("--- Задание 1 ---")
medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации (°C): ")

# Создание и запись в файл recipe.txt
with open("recipe.txt", "w", encoding="utf-8") as f:
    f.write(f"{medium_name}\n")
    f.write(f"- Концентрация агара: {agar_concentration}%\n")
    f.write(f"- Температура стерилизации: {sterilization_temp}°C\n")

print("Файл 'recipe.txt' успешно сформирован!")
print()

# --- Задание 2 ---
print("--- Задание 2 ---")
operator_name = input("Введите имя оператора: ")
pressure_value = input("Введите текущее значение давления (Па): ")

# Создание и запись в файл sensor_log.txt в формате таблицы
with open("sensor_log.txt", "w", encoding="utf-8") as f:
    f.write(f"{operator_name}\t{pressure_value}\n")

print("Данные успешно сохранены в sensor_log.txt")
print()

# --- Итоговое задание (Электронный журнал) ---
print("--- Итоговое задание ---")
researcher_name = input("ФИО исследователя: ")
date = input("Дата: ")
experiment_name = input("Эксперимент: ")
conclusion = input("Вывод: ")

# Формирование красивой рамки и запись в journal.txt
with open("journal.txt", "w", encoding="utf-8") as f:
    f.write("+---------------------------------------------------+\n")
    f.write("| Электронный лабораторный журнал                   |\n")
    f.write("+---------------------------------------------------+\n")
    # Используем <29 для выравнивания текста по левому краю с пробелами
    f.write(f"| ФИО исследователя : {researcher_name:<29} |\n")
    f.write(f"| Дата              : {date:<29} |\n")
    f.write(f"| Эксперимент       : {experiment_name:<29} |\n")
    f.write("+---------------------------------------------------+\n")
    f.write("| Вывод:                                            |\n")
    
    # Простой перенос слов для вывода, чтобы текст не вылезал за рамку
    words = conclusion.split()
    line = "| "
    for word in words:
        if len(line) + len(word) + 1 <= 51:
            line += word + " "
        else:
            f.write(f"{line:<51}|\n")
            line = "| " + word + " "
    if line != "| ":
        f.write(f"{line:<51}|\n")
    
    f.write("+---------------------------------------------------+\n")

print("Журнал успешно сформирован и записан в journal.txt")
print()