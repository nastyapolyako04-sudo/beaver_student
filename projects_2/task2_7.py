# --- Задание 1 (Перебор элементов и добавление даты) ---
print("--- Задание 1 ---")
files = ["seq1", "seq2", "seq3", "seq4"]
# Фиксированная дата взятия образца (можешь поменять на нужную)
sample_date = "_2026-09-29"

for name in files:
    new_name = name + sample_date + ".fasta"
    print(new_name)
print()

# --- Задание 2 (Перебор элементов в строке) ---
print("--- Задание 2 ---")
# Список из нескольких последовательностей
seqs = ["ATATACGCGTA", "CTTCGGNGGA"]

for seq in seqs:
    print(f"Последовательность: {seq}")
    for letter in seq:
        print(letter)
    print("---") # Разделитель между последовательностями
print("Цикл выполнен.")
print()