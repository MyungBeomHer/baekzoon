import heapq
import sys
import math
I = sys.stdin.readline
count = 0
while True:
    N = int(I())
    if N == 0:
        exit(0)

    count +=1
    arr = [list(map(int,I().split())) for _ in range(N)]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    def dijkstra(s_x,s_y):
        D = [[math.inf] * N for _ in range(N)] #N * N 행렬의 D 리스트 생성
        Q = [(arr[0][0],s_x,s_y)] #시작점의 가중치와 좌표를 넣어준다.

        while len(Q) != 0:
            d, u_x,u_y = heapq.heappop(Q) # pop 해주고
            if D[u_x][u_y] <= d: # 기존 값보다 크거나 같다면 볼 필요 x
                continue
            D[u_x][u_y] = d #기존 값보다 작다면 넣어주고
            for i in range(4): #for문 돌리면서 갈 수 있는 곳 가면서
                nx = u_x + dx[i]
                ny = u_y + dy[i]
                if 0<=nx<N and 0<= ny <N: #갈 수 있는 곳이라면
                    heapq.heappush(Q,(d + arr[nx][ny],nx,ny)) #push 넣어줌 걍 bfs네
        return D

    ans = dijkstra(0,0)
    print("Problem {}: {}".format(count,ans[N-1][N-1]))


