# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

n = int(input('Vvedite kol-vo elementov v massive: '))
x = int(input('Vvedite X: '))

list_a = list()
for i in range(n):
    list_a.append(random.randint(1, n+1))

res = list_a[0]
min_diff = abs(int(list_a[0])-x)
for i in range(n):
    if min_diff > abs(int(list_a[i])-x):
        min_diff = abs(int(list_a[i])-x)
        res = int(list_a[i])
print(f'V massive {list_a} blizhayshee po znacheniyu k chislu {x} chislo {res}')