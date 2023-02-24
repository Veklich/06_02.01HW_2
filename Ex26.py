# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# def exponentiation (a, b):
#     res = 1
#     for i in range(1, b+1):
#         res *= a
#     return res

# print(exponentiation(int(input('Vvedite A: ')), int(input('Vvedite B: '))))

def exponentiation(a, b, res=1):
    if b == 0:
        return res
    else:
        res = a * exponentiation(a, b-1, res)
        return res


print(exponentiation(int(input('Vvedite A: ')), int(input('Vvedite B: '))))
