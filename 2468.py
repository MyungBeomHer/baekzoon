import sys
from collections import deque

I =sys.stdin.readline

N = int(input())

G =[]
max_num = 0

for i in range(N):
    G.append(list(map(int,I().split())))
    for j in range(N):
        max_num = max(max_num,G[i][j])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

max_count = 0


def bfs(x_s,y_s,heights):
    Q = deque()
    Q.append((x_s,y_s))
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny<N:
                if G[nx][ny] > heights and visited[nx][ny] == 0:
                    visited[nx][ny] =1
                    Q.append((nx,ny))


for height in range(1,max_num + 1):
    visited = [[0]*N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if G[i][j] > height and visited[i][j] == 0:
                bfs(i,j,height)
                count +=1

    max_count = max(max_count,count)
print(max_count)













