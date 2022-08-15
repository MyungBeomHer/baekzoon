import sys
I = sys.stdin.readline

N = int(I())
arr = list(map(int,I().split()))

a = [0] * 1000001

# 내 높이에 해당하는 화살이 있다면
# -> o
# ----->

# 내 높이에 해당하는 화살 없다면
# x
# ->

# 기존에 내 높이와 같은 곳에서 날아오는 화살이 있다면 그 화살을 사용한 뒤 화살의 높이 - 1을시켜주고
# 내 높이에 해당하는 화살이 없다면 화살 하나를 만들어서 내 풍성을 터트린 뒤 높이 -1 을 시켜준다. 

result = 0
for i in range(N):
    h = arr[i]
    #높이에 해당하는 화살이 날아오고 있을때
    if a[h]:
        a[h] -= 1
        a[h - 1] += 1
    #높이에 해당하는 화살이 하나도 없을때
    else:
        result +=1
        a[h - 1] +=1

print(result)