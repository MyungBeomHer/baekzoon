N = int(input())
W = [0] + list(map(int, input().split()))
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]


def DP(node):
    if visited[node] == 1:
        return max(dp[node][0], dp[node][1])

    visited[node] = 1 #방문
    dp[node][1] = W[node] #이 곳을 색칠 -> 가중치 넣음
    #DP는 재귀 -> 점화식
    for child in tree[node]:
        if visited[child] == 0: #아직 방문 안했더라면
            DP(child) # 재귀 돌리고

            dp[node][0] += max(dp[child][1], dp[child][0]) #색칠 안했을때 -> 아래에서 색칠할 수도 안할 수도 있음

            dp[node][1] += dp[child][0] #색칠 시 -> 아래에서는 무조껀 색칠 못함 -> dynamic 개꿀이네

    return max(dp[node][0], dp[node][1]) #root를 색칠한거랑 안한것중 max 값을 반환


result = DP(1)

check = [0 for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]


def findPath(node, ps):
    if visited[node] == 1:
        return
    visited[node] = 1 #방문 x

    if ps == 1:

        check[node] = 0
        for child in tree[node]:
            if visited[child] == 0:
                findPath(child, 0)

    else:
        if dp[node][0] > dp[node][1]:
            check[node] = 0

            for child in tree[node]:
                if visited[child] == 0:
                    findPath(child, 0)

        else:
            check[node] = 1

            for child in tree[node]:
                if visited[child] == 0:
                    findPath(child, 1)


findPath(1, 0)

print(result)
for i in range(N + 1):
    if check[i] == 1:
        print(i, end=' ')