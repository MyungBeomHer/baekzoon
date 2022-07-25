import sys
from collections import deque
import math
import heapq
#N은 출발지점 K는 도착지점
N,K = map(int,sys.stdin.readline().split())

queue = deque()
queue.append(N)

MAX = 10**5
count_graph = [0] * (MAX + 1)

while queue:
    x = queue.popleft()

    if x == K:
        print(count_graph[x])
        break

    for nx in (x-1,x+1,x * 2):
        if  0 <= nx <= MAX and count_graph[nx] == 0:
            count_graph[nx] = count_graph[x] + 1
            queue.append(nx)


























