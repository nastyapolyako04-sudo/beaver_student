# --- Задание 1 (Расчет калорийности) ---
print("--- Задание 1 ---")
proteins = float(input("Масса белков в продукте (г): "))
fats = float(input("Масса жиров в продукте (г): "))
carbs = float(input("Масса углеводов в продукте (г): "))

# Формула: Кал = (Белки * 4) + (Жиры * 9) + (Углеводы * 4)
calories = (proteins * 4) + (fats * 9) + (carbs * 4)
print(f"Общая калорийность: {calories} ккал")
print()

# --- Задание 2 (Индекс массы тела) ---
print("--- Задание 2 ---")
weight = float(input("Введите ваш вес (кг): "))
height_cm = float(input("Введите ваш рост (см): "))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

print("--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{height_cm:.1f} см")
print(f"Вес:\t{weight:.1f} кг")
print(f"Индекс массы тела: {bmi:.2f}")
print()

# --- Задание 3 (Фасовка препарата) ---
print("--- Задание 3 ---")
total_capsules = int(input("Введите общее количество произведенных капсул: "))
package_capacity = int(input("Введите количество капсул в одной упаковке: "))

full_packages = total_capsules // package_capacity
remaining_capsules = total_capsules % package_capacity

print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packages}")
print(f"Остаток капсул:\t{remaining_capsules}")
print()

# --- Итоговое задание (Приготовление физраствора) ---
print("--- Итоговое задание ---")
volume = float(input("Введите нужный объем раствора (в мл): "))
# Масса соли = объем * 0.009
salt_mass = volume * 0.009

# Вывод в консоль
print("\nОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:")
print(f"Общий объем:\t{volume} мл")
print(f"Масса соли:\t{salt_mass:.2f} г")
print(f"Объем воды:\t{volume} мл")

# Запись в файл
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {volume} мл\n")
    file.write(f"Масса соли: {salt_mass:.2f} г\n")
    file.write(f"Объем воды: {volume} мл\n")
print("\nРецепт успешно сохранен в файл recipe.txt")
print()