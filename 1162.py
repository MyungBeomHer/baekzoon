import sys
import heapq
import math

I = sys.stdin.readline

N,M,K = map(int,I().split())

G = [[] for _ in range(N)]

for _ in range(M):
    u,v,w = map(int,I().split())
    G[u - 1].append((w, v - 1))
    G[v - 1].append((w, u - 1))

def Dijkstra(start):

    D = [[math.inf for _ in range(K + 1)]for _ in range(N)] #이중 리스트로 만들고
    Q = [(0,start,0)] #거리, ~정점 , 포장 횟수
    D[start][0]  = 0

    while len(Q) != 0:

        d,u,count = heapq.heappop(Q)
        if D[u][count] < d:
            continue
        for w,v in G[u]:
            if D[v][count] > d + w:
                D[v][count] = d + w
                heapq.heappush(Q,(d+w,v,count))
            #포장 가능 할 때
            if count < K and D[v][count + 1] > d:
                D[v][count + 1] = d
                heapq.heappush(Q,(d,v,count + 1))

    print(min(D[N-1]))
    return

Dijkstra(0)


































