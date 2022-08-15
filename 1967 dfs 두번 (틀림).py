import sys

I = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(I())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a,b,c = map(int,I().split())
    G[a - 1].append((b - 1,c)) #간선 , 간선 , 가중치
    G[b - 1].append((a - 1,c))


    #현재 정점, 루트로부터 현재까지의 거리 u,d
def dfs(u,d):
    for v,w in G[u]:
        #방문 안했더라면
        if D[v] == -1:
            D[v] = d + w
            dfs(v,d + w)

D = [-1]* n
D[0] = 0
dfs(0,0)

#제일 큰 값의 index를 start 지점으로 지정
s = D.index(max(D))

#reset
D = [-1] * n
#시작부분 0 넣어주기
D[s] = 0
dfs(s,0)

print(max(D))

