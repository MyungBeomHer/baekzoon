N = int(input())

d = [0]*30001 #Dp 테이블 초기화

# 갯수 d[1] = 0
for i in range(2, N+1):
    #이미 뺏다고 가정
    d[i] = d[i-1] + 1 # 3 -> 2 d[3] = d[2] + 1

    if i%2 == 0:
        d[i] = min(d[i],d[i//2] + 1)

    if i%3 ==0:
        d[i] == min(d[i],d[i//3] + 1)

    if i%5 == 0:
        d[i] == min(d[i],d[i//5] + 1)

print(d[N])
