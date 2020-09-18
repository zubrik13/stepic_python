#! /bin/bash/python

figure = input()

if figure == "треугольник":
	a = float(input())
	b = float(input())
	c = float(input())

	p = float(0.5 * (a + b + c))

	square = (p * (p - a) * (p - b) * (p - c)) ** 0.5
	print(square)

elif figure == "прямоугольник":
	a = float(input())
	b = float(input())

	square = a * b
	print(square)

elif figure == "круг":
	pi = 3.14
	r = float(input())

	square = pi * r` ** 2
	print(square)





