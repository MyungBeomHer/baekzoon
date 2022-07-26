import sys

I = sys.stdin.readline
N,M = map(int,I().split())
arr = list(map(int,I().split()))
arr.sort()

a =[0]*M
"""
#중복 되는 거 없이 오름차 순 조합 
def combination(level,idx):
    if level == M:
        print(*a)
        return
    for i in range(idx,N):
        a[level] = arr[i]
        combination(level + 1,idx + 1)
        a[level] = 0
    return
combination(0,0)
"""

#중복되는 거 없이 순열
def bktk(row):
    if row == M:
        print(*a)
        return
    for i in arr:
        if i not in a:
            a[row] = i
            bktk(row + 1)
            a[row] = 0
    return
bktk(0)