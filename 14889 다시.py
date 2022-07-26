import sys

N = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
value = 99

#리스트에 있는 값들을 조건에 의해 더해주는 함수
def sum(L):
    ans = 0
    for i in L:
        for j in L:
            ans += arr[i][j]
    return ans
#조합 함수
#a에 값이 N까지 싸인뒤 재귀값들이 return 되면서 그 다음값인
#b에 값이 쌓인 후 a 와 b에 값이 다 쌓인 후에는 더해준다.
def Combination(row,a,b):
    global value
    if row == N and len(a) == N//2 and len(b) == N//2:
        value = min(value,abs(sum(a) - sum(b)))
    elif row !=N:
        Combination(row + 1, a + [row], b)
        Combination(row + 1, a , b + [row])

#a,b를 리스트 형태로 만들어서 조합이 들어오는 즉시 저장해준다.
Combination(0,[],[])
print(value)