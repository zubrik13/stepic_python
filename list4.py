"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным
"""
l = [i for i in input().split()]

dup = [] # find all duplicates in list
for i in l:
    if l.count(i) > 1:
        if i not in dup:
            dup.append(i)

out = ' '.join([str(j) for j in dup]) # convert list to string
print(out)
