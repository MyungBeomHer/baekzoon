N = int(input())

for i in range(1,N + 1):
    a = list(map(int,str(i)))
    s = i + sum(a)
    if s == N:
        print(i)
        exit(0)
print(0)
