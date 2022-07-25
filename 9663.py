import sys

N = int(input())

#arr[행] = 열
arr = [None] * N

def bktk(row):
    if row == N:
        return 1
    ans  = 0
    #열
    #걍 정해진 행 범위내에서 열 단위로 움직인다고 생각하면 됨
    for i in range(N):
        flag = True
        #행 1*1 -> 2*2 -> 3*3 -> 4*4 -> N*N 범위로 움직이
        for j in range(row):
            if arr[j] == i or j - arr[j] == row - i or \
                    j + arr[j] == row + i:
                flag = False
                break
        #열은 고정 상태에서 행이 원하는 행이면 재귀 돈다고 보면 됨
        if flag:
            arr[row] = i #삽입
            ans += bktk(row + 1) #재귀
            arr[row] = None #복구
    return ans
print(bktk(0))

