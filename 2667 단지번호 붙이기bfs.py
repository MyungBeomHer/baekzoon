import sys
from collections import deque
import heapq

def main():
    input = sys.stdin.readline

    N = int(input())

    graph = []

    for i in range(N):
        graph.append(list(map(int,input().strip()))) #문자열\n문자열\n
        # a = [list(map(int,input().split())) for _ in range(n)] 띄어쓰기 \n 띄어쓰기 \n


    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def bfs(start_x,start_y,num):
        queue = deque()
        queue.append((start_x,start_y))

        graph[start_x][start_y] = num
        count = 1

        while queue:
            x,y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = num
                    count += 1
                    queue.append((nx,ny))

        return count

    number = 1

    Q = []

    for i in range(N):
        for j in range(N):
            #처음 방문 -> number를 넣어줘서 차별
            if graph[i][j] == 1:
                number += 1
                heapq.heappush(Q,bfs(i,j,number))

    print(len(Q))

    while len(Q) != 0 :
        print(heapq.heappop(Q))

if __name__ == '__main__':
    main()