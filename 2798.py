import sys

N,M = map(int,input().split())

arr = list(map(int,sys.stdin.readline().split()))

a = [0] * 3
value = 0
def sum():
    global value
    sum = 0
    for i in a:
        sum += i
    if sum <= M:
        value = max(value,sum)
    return

def bktk(row, idx):
    if row == 3:
        sum()
        return
    for i in range(idx, N):
        a[row] = arr[i]
        bktk(row+1,i+1)
        a[row] = 0
    return

bktk(0,0)
print(value)
