import sys

N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int,sys.stdin.readline().split())))

# N = 2개 부터 시작 1,N넣음
# 내 기준 앞에꺼와 나를 봤을때 가중치가 최솟값이 되는놈을 빨초파에 넣음
for i in range(1,N):
    dp[i][0] = min(dp[i - 1][1] , dp[i -1][2]) + dp[i][0]
    dp[i][1] = min(dp[i- 1][0], dp[i -1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + dp[i][2]
print(min(dp[N-1][0], dp[N-1][1],dp[N-1][2]))
