import sys

N, Q = map(int, sys.stdin.readline().split())

A = int(sys.stdin.readline())  # 정수로 간다
B = int(sys.stdin.readline())

result = []

# C
C = A + B
C = str(C)
if len(C) < N + 1:
    C = '0' + C

for i in range(Q):
    count = 0

    # 입력 및 초기화
    who, index, value = sys.stdin.readline().split() #이렇게 하면 str로 받는 구나
    index = int(index)
    value = int(value)

    if who == 'B':

        str_B = str(B)
        x = str_B[-index]
        x = int(x)

        B -= x * (10 ** (index - 1))
        B += value * (10 ** (index - 1))

    elif who == 'A':
        str_A = str(A)
        x = str_A[-index]
        x = int(x)

        A -= x * (10 ** (index - 1))
        A += value * (10 ** (index - 1))

    # D---------
    D = A + B
    D = str(D)
    if len(D) < N + 1:
        D = '0' + D
    # ---------
    if D == C:
        count = 0

    # D와 C가 다르다면
    else:
        for i in range(len(C)):
            if D[i] != C[i]:
                count += 1
    C = D
    if len(C) < N + 1:
        C = '0' + C
    print(count)
    #result.append(count)

"""
for i in result:
    print(i)
"""