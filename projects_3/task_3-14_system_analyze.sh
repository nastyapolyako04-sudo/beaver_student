#!/bin/bash

df -h | awk 'NR > 1 {
    val = int($5)
    if (val > 90) {
        print $1, $5, "Предупреждение: заполнение более 90%!"
    } else {
        print $1, $5
    }
}'
