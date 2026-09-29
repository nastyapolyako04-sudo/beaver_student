# --- Задание 1 (Счетчик нуклеотидов) ---
print("--- Задание 1 ---")
print("=== Анализ последовательности ДНК ===")
dna_sequence = input("Введите последовательность ДНК: ").upper()

print(f"\nПоследовательность в верхнем регистре: {dna_sequence}\n")

# Подсчет количества
count_a = dna_sequence.count("A")
count_t = dna_sequence.count("T")
count_g = dna_sequence.count("G")
count_c = dna_sequence.count("C")
total_length = len(dna_sequence)

print("Подсчёт нуклеотидов:")
# Вывод количества и процента (процент = количество / общая длина * 100)
print(f"A: {count_a} ({count_a / total_length * 100:.1f}%)")
print(f"T: {count_t} ({count_t / total_length * 100:.1f}%)")
print(f"G: {count_g} ({count_g / total_length * 100:.1f}%)")
print(f"C: {count_c} ({count_c / total_length * 100:.1f}%)")

print(f"\nОбщая длина: {total_length} нуклеотидов")
print()