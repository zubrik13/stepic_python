def f(n):
    return n * 10 + 5

r1 = f(10)

r2 = f(f(10))

r3 = f(f(f(10)))

print(r1, r2, r3)