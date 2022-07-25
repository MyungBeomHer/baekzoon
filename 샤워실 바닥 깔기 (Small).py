import sys

sys.setrecursionlimit(10000)

def main():
    k = int(sys.stdin.readline().rstrip())
    sewer_x,sewer_y = map(int,sys.stdin.readline().split()) #하수구 x,y 좌표

    N = 2 ** k
    #어짜피 우리는 x,y 좌표를 첨부터 알고 있어 -> 꼭 만들고 해야될까? -> 만들면서 채워넣으면 안될까? -> 일단 pass


    #o(n^2) 전역변수
    matrix = []
    for i in range(N):
        matrix = [[0] * N for _ in range(N)]
    matrix[sewer_y-1][sewer_x-1] = -1  #O(1) 생각해봤는데 뒤에서 reverse 씌우면 어짜피 행만 reverse 되니깐 행과 열을 교차한다음 reverse 씌어주면 이렇게 됨

    #2 타일을 채워넣는 법 -> 정사각형 즉, p(k)= (2^k) * (2^k) 인데 k = 1 가 됬을때 색칠하고 종료
    #2-1.x,y 좌표가 이 정사각형 안에 있으면 x,y 좌표를 빼고 색칠
    #2-2.x,y좌표가 없으면 edge부분?만 색칠
    #2-3.나머지 색칠 -> 이러면 시간 복잡도 올라가지 않을까?

    #k는 1,2야 즉, 2*2정사각형을 4칸 아니면 1칸으로 만들 수 있어
    #-> k = 2 라하면 step을 정해서 원하는 칸에 배치 할 수 있잖아?

    #첨부터 하수구의 위치를 알고 시작하면 어떨까?
    def floor(N,x=0,y=0,num=1):
        flag = 0

        if N == 2:
            #2칸씩 이동
            #2*2정사각형으로 쪼갰을때 어느 한부분에는 하수구가 무조껀 있다.
            for i in range(x,x+2):
                for j in range(y,y+2):
                    #0일때가 더 깔끔할 것 같다.
                    #하수구가 있을때로 flag 값을 건드릴 필요가 없다.
                    if matrix[i][j] == -1:
                        flag = 1
                    #채워넣을 수 있는 곳일때
                    if matrix[i][j] == 0:
                        matrix[i][j] = num

            #하수구가 없을때 한부분을 0으로 만들어줘야된다.
            if flag == 0:
                if num == 1:
                    matrix[1][1] = 5
                elif num == 2:
                    matrix[1][2] = 5
                elif num == 3:
                    matrix[2][1] = 5
                else:
                    matrix[2][2] = 5
            return 0 #행렬 다 채웠으니 종료

        else:
        #정사각형으로 쪼개는거지 O(log2N *log2N) 시작부분 보내줌

            for i in range(0,N,2):
                for j in range(0,N,2):
                    floor(N//2,i,j,num)
                    num += 1
            return 0 #완전 종료


    floor(N,0,0,1)
    matrix.reverse()

    for i in range(N):
        for j in range(N):
            print(matrix[i][j],end=' ')
        print()



if __name__ == '__main__':
    main()