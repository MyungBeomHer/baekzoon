import sys

L,C = map(int,input().split())
arr = list(sys.stdin.readline().split())

arr.sort()
a = ['A'] * L
Consonant = ['a','e','i','o','u']

def bktk(row):
    if row == L:
        x,y = 0,0
        #모음
        for i in a:
            if i in Consonant:
                x += 1
            #자음
            else:
                y += 1
        if x>= 1 and y>= 2:
            print("".join(a))
        return
    for i in arr:
        if a[row - 1] < i:
            a[row] = i
            bktk(row+1)
            a[row] = 'a'
    return
bktk(0)


