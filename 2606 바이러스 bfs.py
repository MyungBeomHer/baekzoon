import sys
from collections import deque



def main():

    input = sys.stdin.readline

    N = int(input())
    M = int(input())

    graph = [[] for i in range(N + 1)]

    for i in range(M):
        a,b = map(int,input().split())

        graph[a].append(b)
        graph[a].sort()
        graph[b].append(a)
        graph[b].sort()

    check = [0] * (N+1)

    def bfs(x):
        count = 0
        Q = deque([x])
        check[x] = 1

        while Q:
            y = Q.popleft()

            for i in graph[y]:
                if check[i] == 0:
                    check[i] = 1
                    Q.append(i)
                    count += 1

        return count

    print(bfs(1))


if __name__ == '__main__':
    main()