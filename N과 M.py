import sys

n,m = map(int,sys.stdin.readline().split())
s = []

def sequence(start):
    #길이가 같으면 종료 조건임
    if len(s)  == m:
        print(' '.join(map(str,s)))
        return
    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            sequence(i+1) #1 2 3 4  -> 1 2 3 -> 1 2 3 5 -> 1 2 3 6 //
            s.pop()

sequence(1)






"""
def main():
    N,M = map(int,sys.stdin.readline().split())
    
if __main__ == '__main__':
    main()
"""