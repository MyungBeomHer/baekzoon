import sys
from collections import deque

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
op = list(map(int,sys.stdin.readline().split()))
max_v = -10 **9
min_v = 10**9

#값을 parameter로 전달 하는 방법이 더 빠르고 간결하고 생각하기 좋다.
def dfs(idx,temp):
    global max_v
    global min_v
    if idx == N-1:
        max_v = max(max_v,temp)
        min_v = min(min_v,temp)
        return
    if op[0]>0:
        op[0] -= 1
        dfs(idx + 1, temp + arr[idx + 1])
        op[0] += 1
    if op[1]>0:
        op[1] -= 1
        dfs(idx + 1, temp - arr[idx + 1])
        op[1] += 1
    if op[2]>0:
        op[2] -= 1
        dfs(idx + 1, temp * arr[idx + 1])
        op[2] += 1
    if op[3]>0:
        op[3] -= 1
        dfs(idx + 1, int(temp / arr[idx + 1]))
        op[3] += 1
dfs(0,arr[0])
print(max_v)
print(min_v)