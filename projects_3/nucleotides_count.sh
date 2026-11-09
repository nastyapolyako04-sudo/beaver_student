#!/bin/bash

printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"

for file in *.fasta; do
    if [ ! -s "$file" ]; then
        continue
    fi

    a=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "A" | wc -l)
    t=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "T" | wc -l)
    g=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "G" | wc -l)
    c=$(grep -v "^>" "$file" | tr -d '\n' | grep -o "C" | wc -l)

    printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$a" "$t" "$g" "$c"
done
