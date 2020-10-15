"""
Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать.
Далее считывает n строк с числами x_i, по одному числу в каждой строке. Итого будет n+1 строк.

При считывании числа x_i программа должна на отдельной строке вывести значение f(x_i). Функция f(x) уже реализована
и доступна для вызова.

Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.
"""
import time

start = time.time()


def f(x):
    result = x ** 2
    return result


# via list + dict
n = int(input())
c = 0
l = []
while c != n:
    i = int(input())
    l.append(i)
    c += 1

d = {}
for x in l:
    if x not in d:
        x_i = f(x)
        d[x] = x_i
        print(x_i)
    else:
        print(d.get(x))

# # via 2 lists
# n = int(input())
# c = 0
# l = []
#
# while c != n:
#     i = int(input())
#     l.append(i)
#     c += 1
#
# res = []
# for x in l:
#     x_i = f(x)
#     if x_i not in res:
#         res.append(x_i)
#         print(x_i)
#     else:
#         index = res.index(x_i)
#         print(res[index])


end = time.time()
print(f"Runtime of the program is {end - start} s")







