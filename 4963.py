import sys
from collections import deque

input = sys.stdin.readline

while True:

    w,h = map(int,input().split()) #h가 높이다.

    if w == 0 and h == 0:
        break

    queue_all = deque()
    graph = []
    for i in range(h):
        graph.append(list(map(int,input().split())))
        for j in range(w):
            if graph[i][j] == 1:
                queue_all.append((i,j))


    dx = [1,-1,0,0,-1,-1,1,1]
    dy = [0,0,1,-1,-1,1,-1,1]

    queue = deque()

    def bfs(x_s,y_s):
        queue.append((x_s,y_s))
        graph[x_s][y_s] = 2
        while queue:
            x,y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx <h and 0<= ny <w and graph[nx][ny] == 1:
                    graph[nx][ny] = 2
                    queue.append((nx,ny))

    count = 0
    while queue_all:
        a,b = queue_all.popleft()

        if graph[a][b] == 1:
            bfs(a,b)
            count += 1

    print(count)