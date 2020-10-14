"""Выведите таблицу размером n \times nn×n, заполненную числами от 1 до n^2
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке,
как показано в примере (здесь n=5n=5):
Sample Input:

5
Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""
n = int(input())


def spiral(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m


for i in spiral(n): print(*i)
