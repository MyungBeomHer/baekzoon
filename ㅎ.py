import random

n,m = map(int,input().split())

A_stack = []
B_stack = []
db = []
charcter = []

for i in range(n):
    a = random.randint(1,n)
    A_stack.append(a)

for i in range(1,n+1):
    if i not in A_stack:
        B_stack.append(i)

charcter.append([list(map(input().split()))])
#robot, chain, number 0,1,2
if charcter[0] == 'A':
    if charcter[2] not in A_stack:
        print('NO')
    elif charcter[2] in A_stack:
        db.append(charcter)
        for i in B_stack:
            if i < charcter[2]








