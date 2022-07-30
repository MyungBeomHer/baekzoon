import sys
from collections import deque
I = sys.stdin.readline

#이전 값과 현재 모듈러 연산 한 후의 값을 보내주면 되잖아
def dijsktra(start):
    if start == 1:
        return '1'

    p = [None] * start
    p[1] = (None,None)

    Q = deque([1])

    while len(Q) != 0:
        x = Q.popleft()
        for v in range(2):
            # 10 -> 100 or 101 / 11 -> 110 or 111
            u = (10 * x + v) % start
            if p[u] is None:
                p[u] = (x,v) # 전 단계의 mod 연산 값 ,
                # 무엇을 더 했는지 뒤에 0을 붙였는지 1을 붙였는지 부모에 넣어줌
                Q.append(u)
    #1과 0으로 이루어진 수 중 start로 나눠지는 숫자가 없다. -> 종료
    if p[0] is None:
        return 'BRAk'
    cur = 0
    ans = []
    while cur != 1:
        par,num = p[cur]
        ans.append(str(num))
        cur = par #역추적 업데이트

    ans.append('1')
    return ''.join(ans[::-1])

T = int(I())
for i in range(T):
    N = int(I())
    print(dijsktra(N))

