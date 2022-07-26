import sys
from itertools import combinations

while 1:
    arr = list(map(int,sys.stdin.readline().split()))[1:]
    if not arr:break
    for i in combinations(arr,6):print(*i)
    print()