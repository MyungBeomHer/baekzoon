import heapq
import sys
import math

I = sys.stdin.readline
N,M,X = map(int,I().split())
graph = [[]for _ in range(N)] #정점의 갯수만큼 넣어준다.

for _ in range(M):
    a,b,cost = map(int,I().split())
    graph[a - 1].append((cost,b - 1)) #비용 먼저 넣는다. 여기서 a - 1과 b -1 로 둔 이유는 1,1 이 아닌 0,0으로 지정하기 위해서

#dijkstra
def solve(s):
    D = [math.inf]*N #기존에 들어왔던 값이 더 작은지 판단해야하기 위해서 무한대를 만들어 무조껀 처음 들어오는 값보다 크게 초기값 지정
    Q = [(0,s)] #Q라는 리스트를 힙 형태로 만듦 + 힙은 앞에 값을 기준으로 작용하기 때문에 가중치를 앞에다가 넣음

    while len(Q) != 0: #힙에 값이 없을때까지
        d,u = heapq.heappop(Q) #bfs 같이 먼저 힙에 있는 값을 빼고
        if D[u] <= d: #기존에 들어왔던 값이 더 작거나 같으면 진행할필요가 없으므로 continue
            continue
        D[u] = d #기존에 들어왔던 값보다 작으므로 진행시킨다.
        for w,v in graph[u]: #가중치, 정점 순으로 뽑아온다. (힙은 앞에 값을 기준으로 정렬되어있으므로)
            heapq.heappush(Q,(d+w,v)) #갈 수 있는 값이므로 heappush 를 해준다. 걍 bfs랑 비슷하다고 보면 되네

    return D #리스트 넘겨주고

result =0

for i in range(N):
    go = solve(i) #시작점을 기준으로 다른 점들을 체크
    back = solve(X - 1) #도착점을 기준으로 다른 점들을 체크
    result = max(result, go[X - 1] + back[i]) # 시작점 + 도착점 = 갔다가 오는 시간 여기서 X - 1로 한 이유는 처음에 0,0으로 세팅했기 때문에// back[i]는 i는 0,0 기준으로 세팅이 되어있기 때문에 건드릴필요가 없다. 
print(result)