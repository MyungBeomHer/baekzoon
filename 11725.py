import sys
sys.setrecursionlimit(10 **9)
I = sys.stdin.readline
N = int(input())
G = [[]for _ in range(N + 1)]

for _ in range(N - 1):
    a,b = map(int,I().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N + 1)
def dfs(now,parent):
    visited[now] = parent

    for v in G[now]:
        if v == parent:
            continue
        if visited[v] == False:
            dfs(v,now)

dfs(1,0)

for i in visited:
    if i == 0:
        continue
    print(i)

