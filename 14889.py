import sys
from collections import deque

N = int(input())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
not_ans = []

r = N//2

ans = []
ans_2 = []

Q =deque()
Q.append(10**9)

#ans에 팀이 매겨졌다고 가정
def sum():

    value = 0
    length = len(ans)
    for i in range(length):
        for j in range(i+1,length):
            value += arr[ans[i]][ans[j]]
            value += arr[ans[j]][ans[i]]


    value_1 = 0
    for i in range(length):
        for j in range(i+1,length):
            value_1 += arr[ans_2[i]][ans_2[j]]
            value_1 += arr[ans_2[j]][ans_2[i]]


    if value > value_1:
        Q.append(min(value - value_1,Q.popleft()))
    else:
        Q.append(min(value_1 - value,Q.popleft()))


def nCr(n,r):
    if n == N:
        #자기는 뭐 가지고 있는지 아는데
        #상대팀은 뭐 가지고 있는지 모름
        if len(ans) == r:
            #상대팀 넘버
            for i in range(N):
                if i not in ans:
                    ans_2.append(i)
            sum()
            for i in range(r):
                ans_2.pop()
        return
    ans.append(n)
    nCr(n+1,r)
    ans.pop()
    nCr(n+1,r)
nCr(0,r)

print(Q.popleft())

