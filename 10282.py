import math
import sys
import heapq
I = sys.stdin.readline

for _ in range(int(input())):
    n,d,c = map(int,I().split())
    G = [[] for _ in range(n)]
    for _ in range(d):
        a,b,s = map(int,I().split())
        G[b-1].append((s,a-1))

    def Dijkstr(start):

        Q = [(0,start)]
        D = [math.inf] * n
        while Q:
            d, u = heapq.heappop(Q)
            if D[u] <= d:
                continue
            D[u] = d
            for w,v in G[u]:
                heapq.heappush(Q,(d + w, v))
        return D

    D = Dijkstr(c - 1)
    ans = 0
    count = 0
    for i in D:
        if i != math.inf:
            ans = max(ans,i)
            count +=1
    print(count, end = ' ')
    print(ans)

