import sys
import heapq

I = sys.stdin.readline

a = []

N = int(input())

for _ in range(N):
    start,end = map(int,I().split())
    heapq.heappush(a,(end,start)) #end,start 순 꼭 기억

end_time = 0
count = 0
while len(a):
    time_end, time_start = heapq.heappop(a)
    #시작시간이 이전에 끝나는 시간보다 크거나 같으면 채택
    #이미 heapq를 끝나는 시간 기준대로 힙이 작동하기 때문에
    #시작시간만 기존에 끝난 시간보다 늦으면 ㄱㅊ
    if time_start >= end_time:
        end_time = time_end
        count += 1
print(count)

