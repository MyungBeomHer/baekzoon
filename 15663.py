import sys
from collections import deque

I = sys.stdin.readline

N,M = map(int,I().split())
arr = list(map(int,I().split()))
arr.sort()

a = [0] * M
visited = [False] * N # 받은 값을 썼냐 안썼냐 판단

def bktk(row):
    if row == M:
        print(*a)
        return

    before = 0
    for i in range(len(arr)):
        #이 숫자를 안썼고 만약 99 99라면 이전에 쓴 값에 9를 넣어
        #9 -> 9 /9 -> 9 가 안되게 만든다.
        #9 -> 9입장에서는 9가 먼저 들어왔고
        # 그후 재귀 호출 시 9가 된다.
        #이 때 9 는 9 -> 9로 접근 하려는데
        # 이미 9가 before에 있기 때문에 접근 불가
        if visited[i] == False and before != arr[i]:
            #삽입
            visited[i] = True
            a[row] = arr[i]
            before = arr[i]
            #재귀
            bktk(row + 1)
            #복구
            visited[i] = False
            a[row] = 0
    return
bktk(0)
