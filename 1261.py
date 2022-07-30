import heapq
import sys
from collections import deque
import math

I = sys.stdin.readline

M,N = map(int,I().split())

arr = [list(map(int,I().strip())) for _ in range(N)]
visited = [[math.inf] * M for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def Dijkstra():

    Q = [(0,0,0)] # 거리, row, col

    while len(Q):
        d,x,y = heapq.heappop(Q)
        if visited[x][y] <= d:
            continue
        visited[x][y] = d

        for i in range(4):
            nx = x + dx[i] #row
            ny = y + dy[i]

            if 0<= nx < N and 0<= ny < M:
                heapq.heappush(Q,(d + arr[nx][ny],nx,ny)) #이전까지 온데 중 제일 작은 값 찾기
            #이문제의 초점은 행렬에서 나아갈 수 있는 부분을 인접 그래프로 보는 것이다.
            # 즉 ,상하좌우 모두를 인접 그래프로 보고 다엑스트라를 이용하여
            # 제일 작은 이전까지의 값과 현재의 값을 더한값중 제일 작은 값을 채택하는 다엑스트라를 이용하였다.
    return visited[N-1][M-1]
ans = Dijkstra()
print(ans)
