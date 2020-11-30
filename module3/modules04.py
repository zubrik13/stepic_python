"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".
Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/
Загрузите содержимое последнего файла из набора, как ответ на это задание.
"""
import requests

with open("dataset05.txt") as file:
    for line in file:
        url = line.strip()

link = "https://stepic.org/media/attachments/course67/3.6.3/"

r = requests.get(url)
filename = r.text.split("/")[-1]

# print(filename)

counter = 0
while filename:
    # print(filename)
    r = requests.get(link+filename)
    if r.text.startswith('We'):
        filename = None
    else:
        filename = r.text
        counter += 1


print(counter)

with open("out04.txt", "w") as out:
    out.write(r.text)


# beauty
# import requests
# url, name = 'https://stepic.org/media/attachments/course67/3.6.3/', '699991.txt'
# while name[:2] != 'We':
#     name = requests.get(url + name).text
# print(name)
