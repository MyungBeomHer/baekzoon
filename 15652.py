N,M = map(int,input().split())

arr =[0] * M

def bktk(row):
    if row == M:
        print(*arr)
        return
    #i는 새로 들어올 값
    for i in range(1,N+1):
        #비내림차순 A[1]<=A[2]<= ...<= A[row-1] <=A[row] <=A[M]
        if i >= arr[row - 1]:

            arr[row] = i
            bktk(row + 1)
            arr[row] = 0
    return
bktk(0)

