from fractions import Fraction
import sys

from timeit import default_timer as timer
from datetime import timedelta

I = sys.stdin.readline
N,M = map(int,I().split())


a = [list(map(int,I().split())) for _ in range(N)] # 음료수, 설탕량

def fr(X):
    w,v = X
    return v/w



a.sort(key = fr,reverse=True)


result = 0

for juice_information in a:
    if  M >= juice_information[0]:
        M -= juice_information[0]
        result += Fraction(juice_information[1],1)

    elif M < juice_information[0]:
        result += M * Fraction(juice_information[1],juice_information[0])
        break

print(f'{result.numerator}/{result.denominator}')
#numerator 기약 분수로 나타낼 때 Fraction의 분자.
#denominator 기약 분수로 나타낼 때 Fraction의 분모.

