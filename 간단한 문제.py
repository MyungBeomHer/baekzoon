import sys

def main():
    n,m = map(int,sys.stdin.readline().split()) #m은 끝나는 수를 의미 ,n은 현재를 의미

    A = list(map(int,sys.stdin.readline().split()))

    #tabulaztion? 사용
    #n-1 번째 A행렬꺼 쓰면 되잖아

    # m = 4 -> 0 1 2 3 즉, A[0] 이 A1이라고 생각
    #B = [0] * (m)
    B = [0]
    """
    def simple_example(k):
        if k == 0:
            B[k] = A[k] * n
            return 0
        B[k] = (2**(k-1) + n - 1) // (2**k + n -1) * A[k]
        simple_example(k-1)
    """
    """
    def simple_example(k):
        if k == -1:
            return 0

        B[k] = (1+(n-1)//2**k)*A[k]

        simple_example(k-1)

    simple_example(m-1)
    """

    C = [0]
    def simple_example(k):

        1 + (2**m -1) /n  =  C[k-1] * (A[k] + B[k])/B[k]

    simple_example(m-1)

    for ans in B:
        print(ans, end = ' ')


if __name__ == '__main__':
    main()
