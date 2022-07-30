import math
import sys
import heapq

N,M,K,X = map(int,input().split())

G = [[]for _ in range(N)]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    G[a-1].append((1,b-1))

def Dijkstra(s):
        D = [math.inf] * N
        Q = [(0,s)]
        while len(Q):
            d,u = heapq.heappop(Q)
            if D[u] <= d:
                continue
            D[u] =d
            for w,v in G[u]:
                heapq.heappush(Q,(d + w, v))
        return D

list = Dijkstra(X-1)
flag = 0
for i in range(N):
    # 여기서 최단 거리가 K가 되는 지점들만 찾아서 출력해주면
    # 기존 다엑스트라 문제와 같음
    if list[i] == K:
        flag = 1
        print(i + 1)

if flag == 0:
    print(-1)







