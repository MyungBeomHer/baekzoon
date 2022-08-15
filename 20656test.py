import sys

I =sys.stdin.readline

def nCr(n):
    return (n*(n-1)*(n-2))//6

for _ in range(int(input())):
    N,M = map(int,I().split())
    arr = [list(map(int,I().split())) for _ in range(M)]

    if N<= 3:
        print("TAK")

    if N < 6:
        if nCr(N) <= M:
            print("NIK")
        else:
            print("TAK")

    else:
        if nCr(N) // 2 <= M:
            print("NIK")
        else:
            print("TAK")
       

