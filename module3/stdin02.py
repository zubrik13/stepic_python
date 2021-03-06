"""
Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит
самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

В качестве ответа укажите вывод программы, а не саму программу.

Слова, написанные в разных регистрах, считаются одинаковыми.
"""
with open("dataset02.txt") as file:
    string = ''
    for line in file:
        line = line.strip().lower()
        string += ' ' + line

words = string.split()
d = {}

for w in set(words):
    d[w] = words.count(w)

max_value = max(d.values())  # maximum value
max_keys = [k for k, v in d.items() if v == max_value]

print(f"{max_keys} {max_value}")

# with open("out02.txt", "w") as out:
#     out.write(f   "")
