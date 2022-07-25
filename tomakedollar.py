N,M = map(int,input().split())

array = []
for i in range(N):
    array.append(int(input()))

d = [10001]*(M+1)

d[0] = 0
for i in range(N): # 화폐 종류 먼저 돌기 3개
    for j in range(array[i],M+1): #d table에 값 넣기
        if d[j - array[i]] != 10001: #(i - k) 원을 만드는 방법이 존재하는 경우 즉, d[2,3,7]은 무조껀 d[0] + 1이므로 1이 들어감
            d[j] = min(d[j],d[j-array[i]] + 1) #기존 방법이 편한지 아니면 새롭게 만든 방법 화폐를 더한 방법이 더 작은지 구함

if d[M] == 10001:
    print(-1)
else:
    print(d[M])