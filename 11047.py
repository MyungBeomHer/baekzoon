import sys
I = sys.stdin.readline

N,K = map(int,I().split())

val = [int(I()) for _ in range(N)]



sum = 0

for i in range(len(val) - 1,-1,-1):
    sum += K//val[i]
    K %= val[i]

print(sum)