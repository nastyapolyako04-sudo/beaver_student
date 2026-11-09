#!/bin/bash

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "Ошибка: запустите скрипт с правами суперпользователя (root)!"
        exit 1
    fi
}

check_root

echo "Скрипт запущен от имени root"
