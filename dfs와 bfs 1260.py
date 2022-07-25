#시간 200?
import sys
from collections import deque
import math

def main():

    input = sys.stdin.readline
    N,M,V = map(int,input().split())

    D = [[0] * (N + 1) for i in range(N + 1)] #[[,,,][,,,][,,,]]

    for i in range(M):
        start, end = map(int, input().split())
        D[start][end] = 1
        D[end][start] = 1 #무방향 그래프

    visited = [False] * (N+1) #방문 한 지점만 체크

    def DFS(start):

        visited[start] = True #방문
        print(start , end=' ') #출력

        for i in range(1,N + 1):
            # 방문 안했더라면 갈 수 있다. 얘는 재귀함수이기 때문에 false를 위에다가 적는게 맞지만
            #BFS는 for 문안에서도 돌아가기 때문에 for 문 안에다가 적어줘야된다. !!!
            if D[start][i] == 1 and visited[i] == False: #갈 수 있는 곳중 방문 안한 곳으로 간다.
                DFS(i) #얘는 재귀니깐 방문 했을때만 체크 해줘도 되는구나 for문이 먼저 도는게 아니니깐 (재귀 -> for문 )
        return

    def BFS(start):
        queue = deque([start]) #큐 작성 후 큐에 넣어줌
        visited[start] = True  #방문 했다고 처리 해주고

        while queue:
            visit = queue.popleft() #빼준다음
            print(visit, end = ' ')

            #여기서도 돌 수 있으므로?
            for i in range(N + 1):
                if D[visit][i] == 1 and visited[i] == False:
                    queue.append(i)
                    visited[i] = True #for문 안에서 자체적으로 돌기 때문에 여기서 true를 해준다. 가기만 했고 아직 제대로 간게 아니므로 visited만 true를 넣어주고 출력은 하지 않는다.

        return

    DFS(V)

    print()

    visited = [False] * (N + 1)
    BFS(V)
    return

if __name__ == '__main__':
    main()