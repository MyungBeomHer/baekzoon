import sys
from collections import deque



def main():
    input = sys.stdin.readline
    N,M = map(int,input().split())

    graph = []

    for i in range(N):
        graph.append(list(map(int,input().strip()))) #[,,,,][,,,][,,,] ->문자열로 받을 때 1110001\n10101010

    step_x = [1,-1,0,0]
    step_y = [0,0,1,-1]

    def bfs(start,end):
        q = deque()
        q.append((start,end))

        while q:
            x,y = q.popleft()

            for i in range(4):
                nx = x + step_x[i]
                ny = y + step_y[i]

                if nx <0 or nx >= N or ny <0 or ny >=M:
                    continue
                if graph[nx][ny] == 0:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))


    bfs(0,0)

    print(graph[N-1][M-1])




if __name__ == "__main__":
    main()
