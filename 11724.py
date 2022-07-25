import sys


input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[]for i in range(N + 1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[a].sort()

    graph[b].append(a)
    graph[b].sort()

check = [0] * (N + 1)

def dfs(x):
    check[x] = 1

    for i in graph[x]:
        if check[i] == 0:
            dfs(i)

count = 0
for i in range(1,N + 1):
    if check[i] == 0:
        dfs(i)
        count += 1

print(count)



