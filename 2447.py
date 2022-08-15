
def solve(n):
    if n == 1:
        return ['*']

    star = solve(n//3) #27 -> 9 -> 3 -> 1
    arr = [] #arr를 계속 새롭게 만드는거구나

    #1->3으로 호출 됬을때
    #'***'
    #'* *'
    #'***'
    #3->9이면 위에가 하나의 값으로 들어감
    #0번 인덱스를 가진 리스트 1->3 *3
    #1번 인덱스를 가진 리스트 1->3 + 빈칸*3 + 1->3
    #2번 인덱스를 가진 리스트 1->3 *3
    #즉, 리스트는 계속 새롭게 바뀌돼... 이전 리스트 가지고 와서 반복하는 형태이다.

    for i in star:
        arr.append(i*3)
    for i in star:
        arr.append(i + ' '*(n//3) + i) #빈칸을 n//3 만큼 띄어놓고 i를 넣겠다.
    for i in star:
        arr.append(i * 3)
    return arr

N = int(input())
print('\n'.join(solve(N)))