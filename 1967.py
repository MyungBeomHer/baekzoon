import sys
sys.setrecursionlimit(10 ** 5)

N = int(input())
G = [[] for _ in range(N)]
for i in range(N - 1): #간선 = 정점 -1
    u,v,w = map(int,sys.stdin.readline().split())
    G[u-1].append((v-1,w))
    G[v - 1].append((u- 1, w))

    #a는 현재 정점, p는 부모
    #여기서 지름은 경로 or 루트로부터 제일 먼 두 곳의 거리 중 더 큰 값을 의미
def dfs(a,p):
    d = 0
    fs = []
    for b,w in G[a]:
        #무방향 그래프이므로 단순히 현재 정점이 부모 정점을 못가게 막기 위해  부모 p를 작성했다.
        if b == p:
            continue
        db,fb = dfs(b,a)
        #이전 가장 긴 지름과 dfs를 통해 들어온 현재 가장 긴 지름 중 가장 큰 값 선택
        d = max(d,db)
        fs.append(w + fb) #루트로부터 이전 경로까지의 거리 + 현재 가중치 = 루트 ~ 현재까지의 경로
        #여기까지는 ------> dfs를 통해 리프 노드까지 나아감     
    fs.sort(reverse= True)
    d = max(d,sum(fs[:2])) #루트로부터 제일 먼 두 곳의 거리
    f = 0 if len(fs) == 0 else fs[0] #배열에 아직 추가안해서 비어있다면 0을 반환 아니면 경로중 제일 큰 값을 반환
    return(d,f) #지름 or 경로 중 제일 큰 값, 경로를 반환

print(dfs(0,None)[0])