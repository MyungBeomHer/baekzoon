import sys

N = int(input())
sys.setrecursionlimit(10 ** 9)
tree = [[] for _ in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u - 1].append(v - 1)
    tree[v - 1].append(u - 1)

dp = [[0] * 16 for _ in range(N )] # 10만개 log2 10만 < 17
visit = [False for _ in range(N)]


def DP(x):
    visit[x] = True

    for i in tree[x]:
        if not visit[i]: #부모로도 갈 수 있는 것을 의미
            DP(i)

            # 최소값을 찾아준다.
            for pre_color in range(16):
                m_num = 100000000
                for color in range(16):
                    if pre_color != color: #이전 칼라와 현재 칼라가 다르다면
                        if m_num > dp[i][color]: #이번에 들어온 칼라가 값이 작다면
                            m_num = dp[i][color] #넣어준다.
                dp[x][pre_color] += m_num #이전 칼라에 for 문돌면서 현재 칼라 들에 대해서 제일 작았던 값들을 넣어준다.

    #칼라 가중치 넣기
    for color in range(16):
        dp[x][color] += color + 1
    return

DP(0)
print(min(dp[0])) #tabulation을 이용해 제일 적합한 값을 답으로 출력 




