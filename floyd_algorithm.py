import sys
import math

def main():
    input = sys.stdin.readline
    N = int(input())
    M = int(input())

    D = [[math.inf]*N for i in range(N)]
    for i in range(N): #자기에서 자기로 가는건 거리가 0이므로
        D[i][i] = 0

    for i in range(M):
        a,b,c = map(int,input().split()) #여러개를 한번에 입력 받을때는 split() 사용
        if D[a-1][b-1] > c:
            D[a-1][b-1] = c

    #floyd mershell
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != j:
                    D[i][j] = min(D[i][j],D[i][k] + D[k][j])

    for i in range(N):
        for j in range(N):
            if math.isinf(D[i][j]):
                D[i][j] = 0

    for d in D:
        print(*d)


if __name__ == '__main__' :
    main()