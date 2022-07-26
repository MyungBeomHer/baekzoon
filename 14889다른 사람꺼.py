N = int(input())
s = [[int(x)for x in input().split()]for x in range(N)]
m = 99
def c(l):
    r = 0
    for i in l:
        for j in l:
            r +=s[i][j]
            #어짜피 자기 자신은 0이니깐 상관 없고
    return r

def d(x,a,b):
    global m
    if x == N and len(a) == N//2:
        m = min(m,abs(c(a) - c(b)))
    elif x != N:
        print(a)
        print(b)
        d(x+1,a+[x],b) #먼저 마지막까지 돈 다음
        d(x+1,a,b+[x]) #마지막으로 돈 것들이 재귀 하면서 b에다가 넣어준다. 
d(0,[],[])
print(m)