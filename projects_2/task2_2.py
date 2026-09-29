# --- Задание 1 ---
print("--- Задание 1 ---")
course_name = "Программирование на Python"
current_stage = 2
completed_tasks = 15

print(f"Курс: {course_name}, Этап: {current_stage}, Выполнено задач: {completed_tasks}")
print()

# --- Задание 2 ---
print("--- Задание 2 ---")
user_input = input("Введите данные: ")
processed_input = user_input.upper()

# Вывод со стрелочкой через sep
print(user_input, processed_input, sep=" -> ")
print()

# --- Задание 3 ---
print("--- Задание 3 ---")
# Понятный нейминг (snake_case)
device_name = "oscilloscope"
inventory_number = "102938"
device_condition = "исправен"
device_quantity = 2

print("Прибор\tИнвентарный номер\tСостояние\tКоличество")
print(f"{device_name}\t{inventory_number}\t{device_condition}\t{device_quantity}")
print()

# --- Итоговое задание (task_2-2_inventory_control.py) ---
print("--- Итоговое задание ---")
reagent_name = input("Введите название реактива: ")
reagent_quantity = int(input("Введите количество: "))

report_message = f"Реактив {reagent_name} поступил на склад в количестве {reagent_quantity} шт."
print(report_message)

# Дополнительно: запись отчета в файл
with open("inventory.txt", "w", encoding="utf-8") as f:
    f.write(report_message + "\n")

print("Отчет записан в файл inventory.txt")
print()