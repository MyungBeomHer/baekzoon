N,M = map(int,input().split())

arr =[None] * M

def bktk(row):
    if row == M:
        print(*arr)
        return
    for i in range(1,N + 1):
        arr[row] = i
        bktk(row + 1)
        arr[row] = None
    return
bktk(0)
