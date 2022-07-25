n,m = map(int,input().split())

array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        if mid < i:
            total += i - mid
    if total < m:
        end = mid - 1
    else : #자른 놈들의 합이 예상보다 커 그럼 된거임  + 절단기 높이 낮춰줌
        result = mid
        start = mid + 1

print(result)
