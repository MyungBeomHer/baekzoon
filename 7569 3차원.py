
import sys
from collections import  deque

I = sys.stdin.readline
M,N,H = map(int,I().split())
G =[]
Q = deque([])


for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int,I().split())))
        for k in range(M):
            if tmp[j][k] == 1:
                Q.append([i,j,k])
    G.append(tmp)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

while Q:
    z,x,y = Q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0<= nx <N and 0<= ny < M and 0<= nz <H and G[nz][nx][ny] == 0:
            G[nz][nx][ny] = G[z][x][y] + 1
            Q.append([nz,nx,ny])

count = 0
for i in G:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        count = max(count, max(j))
print(count - 1)





















