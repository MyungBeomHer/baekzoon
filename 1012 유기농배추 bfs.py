import sys
from collections import deque
import heapq


def main():
    input = sys.stdin.readline
    T = int(input())
    for i in range(T) :
        M,N,K = map(int,input().split()) #가로, 세로(행)
        matrix = [[0]*M for i in range(N)]

        for i in range(K):
            x,y = map(int,input().split())
            matrix[y][x] = 1

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        def bfs(start_x,start_y,num):
            queue = deque()
            queue.append((start_x,start_y))

            matrix[start_x][start_y] = num
            while queue :
                x,y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx <0 or nx >=N or ny >= M or ny <0:
                        continue
                    if matrix[nx][ny] == 0:
                        continue
                    if matrix[nx][ny] == 1:
                        matrix[nx][ny] = num
                        queue.append((nx,ny))


        number = 1
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    number += 1
                    bfs(i,j,number)

        print(number -1)


if __name__ == '__main__':
    main()