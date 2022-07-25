import sys
import heapq
import math
from collections import deque

def solve(adj,s):
    D = [math.inf]*len(adj)
    Q = [(0,s)]

    while len(Q) != 0:
        d,u = heapq.heappop(Q)
        if D[u] <= d:
            continue
        D[u] = d
        for w,v in adj[u]: #v는 도착지를 의미
            heapq.heappush(Q,(d+w,v))

    return D




def main():
    input = sys.stdin.readline

    n = int(input()) #도시의 갯수
    m = int(input()) #버스의 갯수

    adj = [[]for i in range(n)]
    rev = [[]for i in range(n)]
    for i in range(m):
        start,dest,dis = map(int,input().split())
        adj[start-1].append((dis,dest-1))
        rev[dest -1].append((dis,start -1))

    source,sink = map(int,input().split())
    source -= 1
    sink -= 1

    D = solve(adj,source)

    path = []
    ptr = sink
    while source != ptr:
        path.append(ptr)
        for w,v in rev[ptr]:
            if D[ptr] == D[v] + w:
                ptr = v
                break

    path.append(source)
    path = path[::-1]

    print(D[sink])
    print(len(path))
    #print(*(i+1 for i in path)) #이게 더 빠르다.
    print(*(i + 1 for i in path))  # 이게 더 빠르다.
    """
    for i in path:
        print(i + 1, end = ' ')
    """





if __name__ == '__main__':
    main()