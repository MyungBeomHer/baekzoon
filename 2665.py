import math
import sys
import heapq

N = int(input())

arr = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def Dijkstra(s_x,s_y):
    D = [[math.inf] * N for _ in range(N)]
    Q = [(0,s_x,s_y)]
    while len(Q):
        d,x,y = heapq.heappop(Q)
        if D[x][y] <= d:
            continue
        D[x][y] = d
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < N:
                #흰방
                if arr[nx][ny] == 1:
                    heapq.heappush(Q,(d,nx,ny))
                #검은방
                if arr[nx][ny] == 0:
                    heapq.heappush(Q,(d + 1,nx,ny))
    return D[N-1][N-1]

ans = Dijkstra(0,0)
print(ans)
