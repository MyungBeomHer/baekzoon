import sys
import heapq

I = sys.stdin.readline

a = []

N = int(input())

for _ in range(N):
    num,start,end = map(int,I().split())
    heapq.heappush(a,(start,end,num))

H_class = [(0,0)] #끝나는 시간,방번호
classroom = [0] * (N + 1)#몇번 방 배정 받을 것인지

while len(a):
    s,e,n = heapq.heappop(a)
    flag = 0
    min_val = 10 ** 9

    #어짜피 끝나는 시간이 제일 빠른 친구가 제일 앞에 온다.
    if H_class[0][0] <= s:
        end,room_idx = heapq.heappop(H_class) #끝나는 시간, 방번호
        heapq.heappush(H_class,(e,room_idx))
        classroom[n] = room_idx

    #제일 빨리 끝나는 친구보다 더 빨리 시작 -> 방개설 필요
    #방개설
    else:
        classroom[n] = len(H_class)
        heapq.heappush(H_class, (e,len(H_class)))
    #heap에 주렁주렁 달려있다해도 제일 빨리 끝난 애들이 앞으로 오기 때문에 걔내만 공략하고 남은 애들은 생각안해도 되잖아?

print(len(H_class))

for i in range(1,N + 1):
    print(classroom[i] + 1)



