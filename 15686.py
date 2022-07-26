import sys
from collections import deque
import heapq

I = sys.stdin.readline
N,M = map(int,I().split())#N은 행 열 M은 살아남을 치킨집 갯수

arr = []
Q =deque()
Q_2 =deque()
Q_1 =deque()
for i in range(N):
    arr.append(list(map(int,I().split())))
    for j in range(N):
        if arr[i][j] == 2:
            Q_2.append((i,j))
        if arr[i][j] == 1:
            Q_1.append((i,j))


arr = [0] * M # Q_2의 순서를 저장하는 리스트 -> nCm

Ans = 10 ** 9 # 초기값 지정
dis = 10 ** 9 #초기값 지정
def cal():
    #집에 대해서 제일 가까운 치킨 집 고르기
    global dis
    global Ans
    total = 0
    for home in Q_1:
        dis = 10**9
        for chicken in result:
            value = abs(chicken[0] - home[0]) + abs(chicken[1] - home[1])
            dis = min(dis,value) #이 치킨집이 집에서 제일 가까움
        total += dis
        #각각의 집을 대상으로 제일 거리가 가까운 치킨집에 대한 거리를 추가함
    Ans = min(Ans,total)

result = [0] * M
def bktk(level,idx):
    if level == M:
        #result 에 값 쌓임
        cal()
        return

    for i in range(idx,len(Q_2)):
        result[level] = Q_2[i]
        # 오름차순 
        bktk(level + 1,i+1)
bktk(0,0)
print(Ans)


