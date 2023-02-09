# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
import random

n = int(input('Vvedite kol-vo elementov v massive: '))
x = int(input('Vvedite X: '))
list_a = list()
for i in range(n):
    list_a.append(random.randint(1, n+1))
print(f'V massive {list_a} chislo {x} vstrechaetsya {list_a.count(x)} raz')