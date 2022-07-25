#시간 186?
import sys
from collections import deque
import math

def main():

    input = sys.stdin.readline
    N,M,V = map(int,input().split())

    D = [[] for i in range(N + 1)] #2개씩 받을 때

    for i in range(M):
        v1, v2 = map(int, input().split())
        D[v1].append(v2)
        D[v2].append(v1) #무방향 그래프이므로

    D_visited = [False] * (N+1)

    for edge in D:
        edge.sort()

    def DFS(start):

        D_visited[start] = True
        print(start , end=' ')

        for i in D[start]:
            if D_visited[i] == False:
                DFS(i)


    def BFS(start):
        B_visited = [False] * (N + 1)
        queue = deque([start])
        B_visited[start] = True

        while queue:
            visit = queue.popleft()
            print(visit, end = ' ')

            #여기서도 돌 수 있으므로?
            for i in D[visit]:
                if B_visited[i] == False:
                    queue.append(i)
                    B_visited[i] = True



    DFS(V)
    print()
    BFS(V)


if __name__ == '__main__':
    main()