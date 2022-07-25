import sys
from collections import deque

I = sys.stdin.readline
M,N,H = map(int,I().split()) #M은 열 N은 행 H는 높이

G = []
Q = deque()
h = N * H
for i in range(h):
    G.append(list(map(int,I().split())))
    for j in range(M):
        if G[i][j] == 1:
            Q.append((i,j))

dx = [-1,1,0,0,N,-N] #행 3 = N (위에 높이) -N(아래 )
dy = [0,0,-1,1,0,0] #열

while Q:
    x,y = Q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <h and 0<= ny <M and G[nx][ny] == 0:
            G[nx][ny] = G[x][y] + 1
            Q.append((nx,ny))

Answer = G[0][0]

for i in range(h):
    for j in range(M):
        if G[i][j] == 0:
            print(-1)
            exit(0)
        Answer = max(Answer,G[i][j])

print(Answer - 1)




