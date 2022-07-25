import sys
import heapq
import math

def Dijsktra(adj, s):
    D = [math.inf]*len(adj)
    Q = [(0,s)] #거리 ,정점 -> 최소힙을 쓰는데 앞부분을 최소힙의 판별 기준으로 잡으려고 :거리가 제일 작은 값이 제일 앞에 온다를 이용
    while len(Q) != 0:
        d,u = heapq.heappop(Q) #시작지 부터 u라는 중간 정점까지의 거리, 시작지 -> u(중간정점) -> 도착정점
        if D[u] <= d: #이 중간정점을 이용한 거리가 이전에 사용한 중간 지점까지의 거리보다 크다면 볼 필요 없이 종료
            continue
        D[u] = d #이 중간정점이 더 짧으므로 업데이트
        for w,v in adj[u]: #이 중간정점을 이용한 인접노드들에 대해서 업데이트
            heapq.heappush(Q,(d+w,v))  #거리,정점을 넣어주면 최소 힙 특성상 작은 값을 먼저 봄,즉, 거리가 제일 짧은 값을 다음 정점으로 놓는다.
    return D

def main():
    input = sys.stdin.readline

    N = int(input())
    M = int(input())

    adj = [[]for i in range(N)]

    for i in range(M):
        s,d,w = map(int,input().split())
        adj[s-1].append((w, d-1)) #[(거리,도착지1) (거리,도착지2) (거리,도착지3) ...(거리,도착지 마지막)]
    start,end = map(int,input().split())
    start -= 1
    end -= 1
    D = Dijsktra(adj, start)
    print(D[end])

if __name__ == '__main__':
    main()