import sys
sys.setrecursionlimit(10**5)

I = sys.stdin.readline
N = int(I())

G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u,v = map(int,I().split())
    G[u].append(v)
    G[v].append(u)

dp = [[0,0] for _ in range (N + 1)]
visited = [False] * (N + 1)
def dfs(x):
    visited[x] = True
    dp[x][0] = 0
    dp[x][1] = 1 #0은 자기 자신 포함 x 1은 자기 자신 포함
    for i in G[x]:
        if not visited[i]:
            dfs(i)
            dp[x][0] += dp[i][1] #현재 기준 자기자신 포함 x 자식은 무조껀 갯수에 포함
            dp[x][1] += min(dp[i][0] ,dp[i][1]) #현재 자기 포함 o -> 자식을 넣은게 작은지 안넣은게 작은지 판단
dfs(1)

print(min(dp[1][0] ,dp[1][1]))

