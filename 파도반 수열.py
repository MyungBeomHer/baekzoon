import sys

def padoban_sequence(N):
    fib = [0] * (101)
    fib[1] = 1
    fib[2] = 1
    if N == 1 or N ==2 :
        return fib[N]

    for i in range(3,N + 1):
        fib[i] = fib[i - 2] + fib[i - 3]
    return fib[N]

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        N = int(sys.stdin.readline())
        print(padoban_sequence(N))

if __name__ == '__main__':
    main()
