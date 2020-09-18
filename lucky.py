#! /bin/bash/python

inp = input()
# inp = "113045"

ls = []

for i in inp:
	num = int(i)
	ls.append(num)

sum1 = ls[0] +ls[1] +ls[2]
sum2 = ls[-1] + ls[-2] + ls[-3]

if sum1 == sum2:
	print("Счастливый")
else:
	print("Обычный")