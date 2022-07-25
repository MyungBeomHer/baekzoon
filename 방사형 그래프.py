import math


def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    temp = x1 * y2 + x2 * y3 + x3 * y1
    temp = temp - y1 * x2 - y2 * x3 - y3 * x1
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0


def check(a):
    n = len(a)
    d = [[0] * 2 for _ in range(n)]
    cos45 = math.cos(45.0 * math.pi / 180.0)
    d[0][0] = 0
    d[0][1] = a[0]
    d[1][0] = cos45 * a[1]
    d[1][1] = cos45 * a[1]
    d[2][0] = a[2]
    d[2][1] = 0
    d[3][0] = cos45 * a[3]
    d[3][1] = -cos45 * a[3]
    d[4][0] = 0
    d[4][1] = -a[4]
    d[5][0] = -cos45 * a[5]
    d[5][1] = -cos45 * a[5]
    d[6][0] = -a[6]
    d[6][1] = 0
    d[7][0] = -cos45 * a[7]
    d[7][1] = cos45 * a[7]

    for i in range(n):
        if ccw(d[i], d[(i + 1) % n], d[(i + 2) % n]) != -1:
            return False
    return True


n = 8
a = list(map(int, input().split()))
order = [i for i in range(n)]
ans = 0
while True:
    b = [a[order[i]] for i in range(n)]
    if check(b):
        ans += 1
    if not next_permutation(order):
        break
print(ans)
