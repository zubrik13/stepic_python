"""
В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики:
они говорили каким-то странным набором звуков.
В какой-то момент один из биологов раскрыл секрет информатиков: они использовали при общении подстановочный шифр,
т.е. заменяли каждый символ исходного сообщения на соответствующий ему другой символ. Биологи раздобыли ключ к шифру
и теперь нуждаются в помощи:

Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита,
на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом,
и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра.
Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%
Sample Output 1:
*d*%*d*#*d*
dacabac

Sample Input 2:
dcba
badc
dcba
badc
Sample Output 2:
badc
dcba
"""

inp1, inp2, inp3, inp4 = input(), input(), input(), input()

# inp1 = 'abcd'
# inp2 = '*d%#'
# inp3 = 'abacabadaba'
# inp4 = '#*%*d*%'

d = dict(zip(inp1, inp2))


def get_key(i):
    for key, value in d.items():
        if i == value:
            return key


def encode(inp):
    out = ""
    for i in inp:
        if i in d.keys():
            out += str(d[i])
    return out


def decode(inp):
    out = ""
    for i in inp:
        if i in d.values():
            out += str(get_key(i))
    return out


out1 = encode(inp3)
out2 = decode(inp4)


print(out1)
print(out2)


"""
a,b,c,d=input(),input(),input(),input()
print(''.join(b[a.index(i)] for i in c))
print(''.join(a[b.index(i)] for i in d))
"""


"""
source, dest = input(), input()
decoded = input()
encoded = input()

print(decoded.translate(str.maketrans(source, dest)))
print(encoded.translate(str.maketrans(dest, source)))
"""