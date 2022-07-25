from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n, m, k = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]
mane = [[-1]*m for _ in range(n)]
sx = -1
sy = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 4:
            sx = i
            sy = j

q = deque()
cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 3:
            q.append((i,j))
            mane[i][j] = 0
            cnt += 1

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if mane[nx][ny] == -1:
                mane[nx][ny] = mane[x][y] + 1
                q.append((nx,ny))

if cnt == 0:
    for i in range(n):
        for j in range(m):
            mane[i][j] = k+1

d = [[-1]*m for _ in range(n)]
d[sx][sy] = 0
q.append((sx,sy))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] != 1 and mane[nx][ny] > k:
                if d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx,ny))

ans = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            if d[i][j] != -1:
                if ans == -1 or ans > d[i][j]:
                    ans = d[i][j]

print(ans)
