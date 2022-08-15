import sys

I = sys.stdin.readline
N = int(input())
bin = int(input())


a = [int(I()) for _ in range(N)] #이렇게 입력받아야 빠르다.


a.sort()
start = 0
end = len(a) - 1

count = 0
while start <= end:
    sum = a[start] + a[end]
    if sum <= bin:
        start += 1
        end -= 1
        count += 1
    else:
        end -= 1
        count += 1
print(count)