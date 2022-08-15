import math
import sys
sys.setrecursionlimit(10 ** 9)
I = sys.stdin.readline
V = int(input())

G = [[] for _ in range(V + 1)]
for _ in range(V):

    a = list(map(int,I().split()))

    for i in range(1,len(a),2):
        if a[i] == -1:break
        else:
            G[a[0]].append((a[i],a[i+1]))

#dfs돌려서 루트로부터 제일 먼지점 찾기
#dfs 돌려서 제일 먼지점에서 제일 먼지점과의 거리 찾기 
visited = [-1] * (V + 1)

def dfs(u):

    for v,w in G[u]:
        if visited[v] == -1:
            visited[v] = visited[u] + w
            dfs(v)

visited[1] = 0
dfs(1)
D = visited.index(max(visited))

visited = [-1] * (V + 1)
visited[D] = 0
dfs(D)
print(max(visited))




