import sys

from collections import deque

I = sys.stdin.readline
dx = [-2,-2,-1,-1,1,1,2,2]
dy =[1,-1,2,-2,2,-2,1,-1]

def bfs(s_x,s_y,e_x,e_y,n):
    G = [[-1]* n for _ in range(n)]
    Q = deque()

    Q.append((s_x,s_y))
    G[s_x][s_y] = 0
    while Q:
        x,y = Q.popleft()
        if x == e_x and y == e_y:
            return G[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <N and 0<= ny <N and G[nx][ny] == -1:
                G[nx][ny] = G[x][y] + 1
                Q.append((nx,ny))





T = int(I())
for i in range(T):
    N = int(I())
    s_a,s_b = map(int,I().split())
    e_a,e_b = map(int,I().split())
    print(bfs(s_a,s_b,e_a,e_b,N))


