import heapq
import math
import sys

I = sys.stdin.readline

N,E = map(int,I().split())

G = [[]for _ in range(N)]
for _ in range(E):
    a,b,c = map(int,I().split())
    G[a-1].append((c,b-1))
    G[b-1].append((c,a-1))
v_1,v_2 = map(int,I().split())

def dijkstra(start):
    D = [math.inf] * N
    Q = [(0,start)]
    while len(Q) != 0:
        d,u = heapq.heappop(Q)
        if D[u] <= d:
            continue
        D[u] = d
        for w,v in G[u]:
            heapq.heappush(Q,(d+w,v))
    return D

#0->x -> y -> N
#0->y->x->N
s = dijkstra(0)
x = dijkstra(v_1 - 1)
y = dijkstra(v_2 - 1)

path_1 =0
if s[v_1 - 1] == math.inf:
    path_1 = math.inf
else:
    path_1 += s[v_1 - 1]
    if x[v_2 - 1] == math.inf:
        path_1 = math.inf
    else:
        path_1 += x[v_2 - 1]
        if y[N-1] == math.inf:
            path_1 = math.inf
        else:
            path_1 += y[N-1]


#path_2 = s[v_2 - 1] + y[v_1 - 1] + x[N-1]
path_2 =0
if s[v_2 -1] ==math.inf:
    path_2 = math.inf
else :
    path_2 += s[v_2 -1]
    if y[v_1 - 1] == math.inf:
        path_2 = math.inf
    else:
        path_2 += y[v_1 - 1]
        if x[N-1] ==math.inf:
            path_2 = math.inf
        else:
            path_2 += x[N-1]

ans = min(path_1,path_2)
if ans == math.inf:
    print(-1)
else:
    print(ans)