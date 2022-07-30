import sys
import heapq

INF = sys.maxsize

n, m, k = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[u].append([v, c])
    nodes[v].append([u, c])

dp = [[INF for _ in range(k+1)] for _ in range(n+1)]
# k번 포장했을 때 n번 노드로 가는 최솟값 dp[n][k]
pq = [[0, 1, 0]]

while pq:
    cur_cost, cur_node, cur_k = heapq.heappop(pq)

    if dp[cur_node][cur_k] < cur_cost: continue

    for next_node, next_cost in nodes[cur_node]:
        if dp[next_node][cur_k] > cur_cost + next_cost:
            dp[next_node][cur_k] = cur_cost + next_cost
            pq.append([cur_cost + next_cost, next_node, cur_k])
            # 포장하지 않고 이번 노드를 사용했을 때
        if cur_k < k:
            if dp[next_node][cur_k+1] > cur_cost:
                dp[next_node][cur_k + 1] = cur_cost
                pq.append([cur_cost, next_node, cur_k+1])
                # 포장 가능하다면 포장한 거리도 큐에 넣는다.

print(min(dp[n]))
# k개 이하를 포장했을 때 n번 노드로 가는 최솟값 출력