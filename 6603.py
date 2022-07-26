import sys

while True:
    arr = list(map(int,sys.stdin.readline().split()))
    if arr[0] == 0:
        break
    N = arr[0]
    a = [0] * 6

    def Combination(row):
        if row == 6:
            print(*a)
            return

        for i in range(1,N + 1):
            if a[row - 1] < arr[i]:
                a[row] = arr[i]
                Combination(row+1)
                a[row] = 0
        return

    Combination(0)
    print()


