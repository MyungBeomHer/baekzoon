import math
import sys
import heapq

I = sys.stdin.readline
for i in range(int(input())):
    n,m,t = map(int,I().split()) #정점, 간선, 목적지갯수
    s,g,h = map(int,I().split()) #출발지 , 거쳐야되는 곳1 , 거쳐야되는 곳 2
    G = [[] for _ in range(n)]
    for _ in range(m):
        a,b,d = map(int,I().split())
        G[a-1].append((d,b-1))
        G[b-1].append((d,a-1))

    des = []
    for _ in range(t):
        des.append(int(I()))

    def Dijkstra(start):
        D = [math.inf] * n
        Q = [(0,start)]
        while len(Q) != 0:
            d,u = heapq.heappop(Q)
            if D[u] <= d:
                continue
            D[u] = d
            for w,v in G[u]:
                heapq.heappush(Q,(d + w, v))
        return D

    # s -> g -> h -> 목적지 1,2 min
    # s -> h -> g -> 목적지 2,1 min
    # i는 도착지

    dests = []

    start = Dijkstra(s - 1)
    start_g = Dijkstra(g - 1)  # g에서 시작
    start_h = Dijkstra(h - 1)  # h에서 시작

    for i in des:
        #s -> g -> h -> i // s -> h -> g -> i
        #경로가 없을때를 지정안해줘서 틀림 -> 아니 문제에 무조껀 최당경로로 가는 길이 하나는 있다매 !!!!
        if start[i-1] != math.inf:
            if start[g - 1] + start_g[h-1] + start_h[i - 1] == start[i-1] or start[h - 1] + start_h[g-1] + start_g[i - 1] == start[i-1]:
                dests.append(i)

    dests.sort()
    for i in dests:
        print(i, end = ' ')
    print()


