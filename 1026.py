import heapq
import sys

I = sys.stdin.readline

N = int(input())
A = list(map(int,I().split()))
B = list(map(int,I().split()))

H = []


heapq.heapify(A)
ans = 0
while len(B):
    ans += max(B) * heapq.heappop(A)
    B.pop(B.index(max(B)))

print(ans)
