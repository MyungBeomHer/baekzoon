import sys

sys.setrecursionlimit(10000)

num = 0

def main():
    k = int(sys.stdin.readline().rstrip())
    sewer_x,sewer_y = map(int,sys.stdin.readline().split()) #하수구 x,y 좌표

    N = 2 ** k #정사각형 한변의 길이

    matrix = [[0 for _ in range(N)] for _ in range(N)]

    matrix[sewer_y-1][sewer_x-1] = -1  #O(1) 생각해봤는데 뒤에서 reverse 씌우면 어짜피 행만 reverse 되니깐 행과 열을 교차한다음 reverse 씌어주면 이렇게 됨

    #정사각형을 쪼개면 이런식으로 공간이 매꿔진다 즉, 2*2인 정사각형일때는 1자리는 비는데 4*4일때는 2*2인 정사각형 4개로 나눌시 여기서 한 정사각형 안에는
    #무조껀 하수구가 들어가게 된다. 이때 나머지 3개의 정사각형은 의도치 않게 한자리씩 비게 되는데 빈 자리인 한자리씩을 모으게 만들면 3개로 이루어진
    #|
    # -- 가 나오게 되는데 이곳을 매꾸면 된다.

    #4개로 쪼갠 정사각형 중 어느 위치에 하수구가 있는지 판단 할꺼다.
    #-1 이 있다면 하수가 있다는 뜻으로 여기는
    def check(s,x,y):
        for i in range(x,x+s):
            for j in range(y,y+s):
                if matrix[i][j] != 0:
                    return False
        return True #하수구나 이미 안 칠한곳임을 의미 -> 즉, 칠 할 수 있다는 의지를 보여줌

    #쪼개진 정사각형 위치당 분면 이름
    #1 3
    #2 4
    #각 수치당 분면이라고 부름
    def floor(N,x=0,y=0):
        global num
        num += 1
        s = N//2 #우리는 정사각형을 1/4로 쪼갤것이다.
        # 즉, 한변의 길이당 1/2씩 줄이면 1/2 * 1/2 = 1/4,으로
        # s는 쪼갠 후 정사각형 한변의 길이를 의미한다.
        if check(s,x,y) :
            matrix[x+s-1][y+s-1] = num #1사분면의 빈 곳에 할당
        if check(s,x+s,y):
            matrix[x+s][y+s-1] = num #2사분면의 빈 곳에 할당
        if check(s,x,y+s):
            matrix[x+s-1][y+s] = num #3사분면의 빈 곳에 할당
        if check(s,x+s,y+s):
            matrix[x+s][y+s] = num #4사분면의 빈곳에 할당
        #한변의 길이가 2인 상태에서 색칠을 했다면 더 할 필요가 없으므로 종료 시켜준다.
        if N == 2:
            return

        floor(s,x,y)
        floor(s,x+s,y)
        floor(s,x,y+s)
        floor(s,x+s,y+s)

    #여기서 부터 시작
    floor(N)
    matrix.reverse()
    """
    for i in matrix:
        print(*i) #이게 되는군요 요호호 어찌보면 주소에 있는 값 가져오는 것이니깐 일리가 있음
    """
    for i in range(N):
        for j in range(N):
            print(matrix[i][j],end=' ')
        print()


if __name__ == '__main__':
    main()