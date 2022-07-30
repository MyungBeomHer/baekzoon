from collections import deque


def solve(N):
    if N == 1:
        return '1'

    Q = deque([1])
    P = [None] * N
    P[1] = (None,None)
    while Q:
        x = Q.popleft()

        for v in range(2):
            u = (x*10 + v)%N
        #bfs로 만들어서 visited 안했더라면
            if P[u] is None:
                P[u] = (x,v) #전단계랑 1과 0중 뭘 붙였는지 알려줌
                Q.append(u)
    if P[0] is None:
        return 'BRAK'
    cur = 0
    ans = []
    while cur != 1:
        par, num = P[cur] #이전 값과 뭘 붙였는지
        ans.append(str(num))#업데이트 1 -1-> 3 -0-> 5 -1-> 0 이라면 1 0 1 순으로 추가해주고 마지막에 1을 넣어 시작점까지 넣어준다.
        cur = par   #0 -> 5 -> 3 -> 1

    ans.append('1')
    return ''.join(ans[::-1]) #역순으로 저장됬으니 역순으로 보내준다.

for i in range(int(input())):
    print(solve(int(input())))
