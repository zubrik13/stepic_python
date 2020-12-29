"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество
d известных нам слов, после чего на d строках указываются эти слова. Затем передаётся количество
l строк текста для проверки, после чего l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:
stepic
champignons
the
"""

import time

start = time.time()

n1 = int(input())
# d = dict()
# d.update(words=[])

st = set()

for i in range(1, n1 + 1):
    st.add(input().lower())

n2 = int(input())

lst = []
for i in range(1, n2 + 1):
    lst.append(input().lower().split(' '))

out = set()
for l in lst:
    for i in l:
        if i not in st:
            out.add(i)

for i in out:
    print(i)


end = time.time()
print(f"Runtime of the program is {end - start} s")


"""
dic = {input().lower() for i in range(int(input()))}

wrd = set()
for w in range(int(input())):
    wrd |= {i.lower() for i in input().split()}

print(*wrd.difference(dic), sep="\n")
"""