import math
import sys
import heapq

I = sys.stdin.readline
V,E = map(int,I().split()) #정점, 간선 갯수
K = int(I()) #시작점

G = [[] for _ in range(V)]

for i in range(E):
    u,v,w = map(int,I().split()) #시작점, 도착점, 가중치
    G[u-1].append((w,v - 1)) #시작점 , 가중치 , 도착점

def dijkstra(start):
    D = [math.inf] * V
    Q = [(0,start)]

    while len(Q) !=0:
        d,u = heapq.heappop(Q)
        if D[u] <= d:
            continue
        D[u] = d
        for w,v in G[u]:
            heapq.heappush(Q,(d + w,v))
    return D


ans = dijkstra(K - 1)

for i in ans:
    if i == math.inf:
        print("INF")
    else:
        print(i)
