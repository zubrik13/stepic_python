"""
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка
"download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится,
надо отправить в качестве ответа на эту задачу.
"""
import re

with open("dataset01.txt") as file:
    for line in file:
        line = line.strip()
        print(line)

r = re.split('(\d+)', line)
inp = r[:-1]

out_str = ''

last_letter = None
for num, val in enumerate(inp):
    if num % 2 == 0:
        last_letter = val
    else:
        out_str += last_letter * int(val)

with open("out01.txt", "w") as out:
    out.write(out_str)


# print(out)

# keys = re.split('[^a-z]', line)
# while("" in keys) :
#     keys.remove("")
#
# values = re.split('[a-z]', line.lower())
# while("" in values) :
#     values.remove("")
#
# tupl = [(key, value) for key, value in zip(keys, values)]
#
# string = ''
# for key in tupl:
#     string += key[0] * int(key[1])
