#88

#1st.입력 받을때 링크드로 받으면서 마지막에 sort가 아닌
#받을때마다 즉각적으로 sort를 해준다.

#2nd. dfs
#

#3nd.bfs
# 방문 ->재귀로 사용

import sys
#sys.setrecursionlimit(9999)
input = sys.stdin.readline
from collections import deque

N,M,V = map(int,input().split())
visit_dfs = [0]*(N + 1)
visit_bfs = [0]*(N + 1)
N_ = [[]for i in range(N + 1)]

#stack = [V]

for i in range(M):
    a,b = map(int,input().split())
    N_[a].append(b)
    N_[a].sort() #추가할때 sort 해야 빠르다.

    N_[b].append(a)
    N_[b].sort()

def dfs (n):
    print(n,end = ' ')
    visit_dfs[n] = 1
    for i in N_[n]:
        if visit_dfs[i] == 0:
            dfs(i)

def bfs(n):
    Q = deque([n])
    visit_bfs[n] = 1

    #왜 재귀를 쓰는게 더 빠를까? 
    while Q:
        x = Q.popleft()
        print(x,end = " ")
        for i in N_ [x]:
            if visit_bfs[i] == 0:
                visit_bfs[i] = 1
                Q.append(i)

dfs(V)
print()
bfs(V)






