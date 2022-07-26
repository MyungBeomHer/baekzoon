import sys

I =sys.stdin.readline

N,M = map(int,I().split())

arr = list(map(int,I().split()))
arr.sort()

a = [0] * M
def bktk(row):
    if row == M:
        print(*a)
        return
    for i in arr:
        if a[row - 1] <= i:
            a[row] = i
            bktk(row + 1)
            a[row] = 0
    return

bktk(0)