original_num = set(range(1,10001)) # 1부터 10000까지의 숫자가 set에 저장됨
visited = set()
for i in range(1,10001):
    # 숫자 -> 문자열 -> 숫자 + 숫자
    # 480 -> 480 + 4 -> + 8 -> + 0
    for j in str(i):
        i += int(j)
    visited.add(i)

ans = sorted(original_num - visited) #set끼리 빼는 것은 차집합을 생각하면 됨
for i in ans:
    print(i)






