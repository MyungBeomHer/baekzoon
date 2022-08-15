import sys
sys.setrecursionlimit(10 ** 9)


I =sys.stdin.readline

for _ in range(int(input())):
    N,M = map(int,I().split())
    arr = [list(map(int,I().split())) for _ in range(M)]

    #이거 안되면 오름차순으로 해야됨
    flag = 0
    a = [0] * 3
    b = []
    def bktk(row , idx):
        global flag
        if flag == 1:
            return

        if row == 3:
            count = 0
            for i in range(M):
                if a != arr[i]:
                    count +=1
            #for문 다 돈다음에 다 틀렸다면
            if count == M:
                for i in range(1,N + 1):
                    if i not in a:
                        b.append(i)
                if len(b) >= 3:
                    List1 = set(b)
                    pred_count = len(b) - 3
                    for i in range(M):
                        List2 = set(arr[i])
                        if len(List1 - List2) != pred_count:
                            b.clear()
                            print("12")
                            return
                    #특정조건 만족하면 flag = 1
                    print("13")
                    flag = 1
                else:
                    flag = 1
            return

        for i in range(idx,N + 1):
            a[row] = i
            bktk(row + 1 , i + 1)
            a[row] = 0
        return
    bktk(0, 1)
    if flag == 1:
        print("TAK")

    elif flag ==0:
        print("NIE")

