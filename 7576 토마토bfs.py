import sys
from collections import deque

def main():
    I = lambda:map(int,sys.stdin.readline().split())

    M,N = I()

    count = 0

    queue = deque([])
    graph = []
    for i in range(N):
        graph.append(list(I()))
        for j in range(M):
            if graph[i][j] == 1:
                queue.append([i,j])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft()
        Answer = graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = Answer + 1
                queue.append([nx,ny])

    for i in graph:
        if 0 in i:
            Answer = 0
            break
    print(Answer - 1)









if __name__ == '__main__':
    main()