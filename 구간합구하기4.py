from collections import deque
import sys

n,m = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))
sum = 0
sum_array =[0]

for x in array:
    sum += x
    sum_array.append(sum)

for i in range(m):
    i,j = map(int,sys.stdin.readline().split())
    result = sum_array[j] - sum_array[i-1]
    print(result)

