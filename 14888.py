import sys
from collections import deque

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
op = list(map(int,sys.stdin.readline().split()))

op_sq = [None] * (N-1)

Q_max = deque()
Q_min = deque()
Q_max.append(-10**9)
Q_min.append(10**9)
#calculate와 ?
def cal():
    value = arr[0]
    for i in range(1,N):
        if op_sq[i-1] == 0:
            value += arr[i]

        elif op_sq[i-1] == 1:
            value -= arr[i]

        elif op_sq[i-1] == 2:
            value *= arr[i]

        elif op_sq[i-1] == 3:
            value = int(value/arr[i])

    Q_max.append(max(value,Q_max.popleft()))
    Q_min.append(min(value,Q_min.popleft()))
    return

#bktk를 나누면 어떨까?
def bktk(row):
    #연산자의 갯수를 row로 본다.
    if row == N - 1:
        cal()
        return
    for i in range(4):
        if op[i] >= 1:
            #삽입
            op_sq[row] = i
            op[i] -= 1
            #재귀
            bktk(row + 1)
            #복구
            op_sq[row] = None
            op[i] += 1
    return

bktk(0) #2개 일때 연산자 1개만 들어오면 됨 -> 즉, 0일때 한번 넣고 1로 가서 더 넣을 연산자가 없음
print(Q_max.popleft())
print(Q_min.popleft())
