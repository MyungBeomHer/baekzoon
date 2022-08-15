import sys, heapq

input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
lecture = [0 for _ in range(n+1)]
arr.sort(key=lambda x: (x[1], x[2])) #시작시간 기준으로 정렬하되
# 시작시간이 같다면 끝나는 시간이 더 빠른 기준으로 잡는다.
room = []
for i in range(1, n+1):
    heapq.heappush(room, i)


minHeap = []
for x in arr:
    #제일 빨리 끝나는 시간이 요번에 온놈보다 빨리 끝난다면 
    while minHeap and minHeap[0][0] <= x[1]:
        end, r = heapq.heappop(minHeap)
        heapq.heappush(room, r)

    r = heapq.heappop(room)
    heapq.heappush(minHeap, [x[2], r]) #끝나는 시간, 방번호 순서대로 넣음 
    lecture[x[0]] = r #강의 번호에 방번호를 넣음 

print(max(lecture))
for x in lecture[1:]:
    print(x)


