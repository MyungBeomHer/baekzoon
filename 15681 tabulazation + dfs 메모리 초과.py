import sys
I = sys.stdin.readline
sys.setrecursionlimit(10 ** 5) # pypy3에서는 5로 해야 메모리 초과 안뜸 python3에서는 더 커야 메모리 초과 안뜨고 

N,R,Q = map(int,I().split())

G = [[]for _ in range(N)]
for _ in range(N-1):
    u, v = map(int,I().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

count = [-1] * N
def dfs(v):
    count[v] = 1 #자식 노드에 도달하면 자식노드가 1이 되므로
    for i in G[v]: #자식으로 가면서
        if count[i] == -1: #방문 안했더라면
            count[v] += dfs(i) #서브트리의 갯수를 서브트리 루트 노드에 넣어준다,
            #노드가 자식이 3개라면
            #count[v] = 1
            #count[v] += 1 (자식1)
            #count[v] += 1 (자식2)
            #count[v] += 1(자식3) 해서 count[v] = 4 가 된다. (자신까지 포함해서)
    return count[v]


dfs(R - 1)

for _ in range(Q):
    ans = int(I())
    print(count[ans - 1])