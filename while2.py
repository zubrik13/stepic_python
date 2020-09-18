a = abs(int(input()))
b = abs(int(input()))

d = 1

while (d % a != 0) or (d % b != 0):
	d +=1
else:
	print(d)

