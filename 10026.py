import sys

I = sys.stdin.readline
sys.setrecursionlimit(3000)
N = int(I())

G = []
for i in range(N):
    G.append(list(I().strip()))

mane =[[0]*N for i in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    mane[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y+ dy[i]
        if 0<= nx <N and 0<=ny <N and G[nx][ny] == G[x][y] and mane[nx][ny] == 0:
            mane[nx][ny] = 1
            dfs(nx,ny)

crazy_mane =[[0]*N for i in range(N)]
def crazy_dfs(x,y):
    crazy_mane[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and crazy_mane[nx][ny] == 0:
            if G[nx][ny] == 'B':
                if G[nx][ny] == G[x][y]:
                    crazy_mane[nx][ny] = 1
                    crazy_dfs(nx,ny)
            else:
                if G[x][y] == 'R' or G[x][y] =='G':
                    crazy_mane[nx][ny] = 1
                    crazy_dfs(nx, ny)


count = 0
crazy_count = 0
for i in range(N):
    for j in range(N):
        if mane[i][j] == 0:
            dfs(i,j)
            count +=1
for i in range(N):
    for j in range(N):
        if crazy_mane[i][j] == 0:
            crazy_dfs(i,j)
            crazy_count +=1


print(count, end = ' ')
print(crazy_count)