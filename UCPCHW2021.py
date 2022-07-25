N,Q = map(int,input().split())

A = int(input()) #정수로 간다
B = int(input())

result = []

#C
C = A + B
C = str(C)
if len(C) < N + 1:
    C = '0' + C

for i in range(Q):
    count = 0

    #입력 및 초기화
    who,index,value = input().split()
    index = int(index)
    value = int(value)

    if who == 'B':

        str_B = str(B)
        x = str_B[-index]
        x = int(x)
        
        B -= x*(10**(index-1))
        B += value*(10**(index-1))
        
    elif who == 'A':
        str_A = str(A)
        x = str_A[-index]
        x = int(x)

        A -= x*(10**(index-1))
        A += value *(10**(index-1))

    #D---------
    D = A + B
    D = str(D)
    if len(D) < N + 1:
        D = '0' + D
    #---------
    if D == C:
        count = 0

    #D와 C가 다르다면
    else :
        for i in range(len(C)):
            if D[i] != C[i]:
                count += 1
    C = D
    if len(C) < N + 1:
        C = '0' + C

    result.append(count)

for i in result:
    print(i)
