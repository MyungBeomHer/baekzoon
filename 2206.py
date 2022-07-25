#for문 돌면서 한부분을 0으로 놓고 bfs 돌리면 됨
#처음 입력 받을때 1값의 위치를 deque에다가 저장한 뒤 순서대로 작동
#벽을 부수지 않았을때와 비교
#더 큰 값을 출력

import sys
from collections import deque

I = sys.stdin.readline
N,M = map(int,I().split())

G = []
Q = deque()

for i in range(N):
    G.append(list(map(int,I().strip())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

def bfs(a,b,c):
    Q.append((a,b,c))

    while Q:
        x,y,z = Q.popleft()
        if x == N -1 and y == M - 1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <N and 0<= ny < M:
                #벽 아직 안깬 상태에서 깨고 들어간다.
                if G[nx][ny] == 1 and z == 0:
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    Q.append((nx,ny,1))
                elif G[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    Q.append((nx,ny,z))

    return -1

print(bfs(0,0,0))






































