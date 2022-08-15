# 즉, 가방에 들어갈 수 있는 보석 들을 저장소에 넣고 그 보석 중 제일 비싼 보석을 찾는다.
import sys,heapq
I = sys.stdin.readline
N,K = map(int,I().split())

stone = [list(map(int,I().split()))for _ in range(N)] #M,V 무게, 가격
bag = [int(I()) for _ in range(K)] #무게

stone.sort() #제일 가벼운 무게 순으로 놓는다.
bag.sort() #제일 작은 가방
storage = []

result = 0 #값 저장
for weight in bag:
    # 제일 가벼운 가방에 넣을 수 있으면 다음 가방에도 넣을 수 있다로 focus
    # 여기서 함정은 제일 비싼 보석이 아니라 제일 가벼운 보석 부터 넣어서
    # 이 가방에 들어갈 수 있는 것 중 제일 비싼 보석을 maxheap을 통해 찾아주는 알고리즘이다.
    while stone and weight >= stone[0][0]: #즉 이 과정은 이 가방에 들어갈 수 있는 보석들을 찾아주는 과정
        heapq.heappush(storage, -stone[0][1]) # 가격을 저장
        heapq.heappop(stone)
    if storage: #들어간 보석 중 제일 비싼 보석을 찾는다.
        result += heapq.heappop(storage)
    elif not stone:
        break


print(-result)