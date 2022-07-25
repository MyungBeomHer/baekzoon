import sys

def sum(a,b):
    return a + b

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        a,b = map(int,sys.stdin.readline().split())
        print(sum(a,b))

if __name__ == '__main__':
    main()
