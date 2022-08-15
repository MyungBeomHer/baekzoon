import sys
sys.setrecursionlimit(10 ** 4)
I = sys.stdin.readline

N = int(input())

a = list(map(int,I().split()))

P = int(input())

G = [[] for _ in range(N)]

root = 0
for u in range(N):
    if a[u] == -1:
        root = u
        continue
    G[a[u]].append(u)

if P == root:
    print(0)
    exit(0)


visited = [False] * N

#리프노드의 갯수
count = 0
def dfs(root, parent):
    global count
    # 삭제할 노드를 만나면 더 이상 안나가면 알아서
    # 자식 노드들도 안만들어짐
    #내가 없애야될 노드야 -> 그럼 종료 -> 자식 안만들어짐
    if root == P:
        return

    visited[root] = True
    #자식 없어 -> 리프 노드
    if len(G[root]) == 0:
        count += 1
        return
    #자식 하나인데 없애는 노드야 -> 리프노드
    if len(G[root]) == 1:
        if P in G[root]:
            count +=1
            return
    for v in G[root]:
        if  v == parent:
            continue
        if visited[v] == False:
            dfs(v,root)
        #얘를 가지고 있는 부모는 한명밖에 없어


dfs(root,-1)
print(count)





