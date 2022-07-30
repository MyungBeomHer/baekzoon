import heapq
import math

N, K = map(int,input().split())

def dijkstra(start, end):
    D = [False] * (100001)
    D[start] = True
    Q = [(0,start)]

    while len(Q) !=0 :
        t, u = heapq.heappop(Q) #가중치(횟수)와 정점
        if u == end:
            print(t) #end에 도착했다면 그때의 가중치 값을 계산
            break

        for nx in (u*2,u+1,u-1):
            if 0<= nx <len(D) and D[nx] == False:
                D[nx] = True
                if nx == u*2: #*2로 순간이동 할때는 0초 걸리므로
                    heapq.heappush(Q,(t,nx))
                else: #u + 1 , u - 1로 이동할때는 1초 걸리므로
                    heapq.heappush(Q,(t+1,nx))


dijkstra(N,K)

