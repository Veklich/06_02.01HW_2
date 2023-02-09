# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12

dict_1 = \
    {
        "1": "А" "В" "Е" "И" "Н" "О" "Р" "С" "Т" "A" "E" "I" "O" "U" "L" "N" "S" "T" "R",
        "2": "Д" "К" "Л" "М" "П" "У" "D" "G",
        "3": "Б" "Г" "Ё" "Ь" "Я" "B" "C" "M" "P",
        "4": "Й" "Ы" "F" "H" "V" "W" "Y",
        "5": "Ж" "З" "Х" "Ц" "Ч" "K",
        "8": "Ш" "Э" "Ю" "J" "X",
        "10": "Ф" "Щ" "Ъ" "Q" "Z"
    }
word = list(input('Vvedite slovo: ').upper())
summa = 0
for i in range(len(word)):
    for j, k in dict_1.items():
        if k.find(word[i]) != -1:
            summa += int(j)
print(f'Stoimost vvedennogo slova ravna: {summa}')
