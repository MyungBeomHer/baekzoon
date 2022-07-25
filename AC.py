import sys
from collections import deque

def main():
    T = int(sys.stdin.readline())

    for i in range(T):
        p = sys.stdin.readline().rstrip() #OK
        size = int(sys.stdin.readline().rstrip())
        array = sys.stdin.readline().rstrip().strip('[]').split(',')

        queue = deque(array)
        # count 가 짝수이면 1,2 -> R 두번 들어왔으므로 reverse 할 필요 없음 reverse가 시간 복잡도 많이 드므로;;;
        # count 를 확인 할 때는 마지막과 'D'과 왔을때다.
        # 즉, 'D'가 오면 count를 확인하여 짝수이면 reverse 할 필요가 없다고 느끼고 delete만 해주고
        # 홀 수 이면 reverse 해주고 delete 해주면 된다.
        # deque 만들 생각이 없었는데 deque의 popleft가 O(1)이고 del array[0]는 O(N)이라길래 깜짝 놀라서 바꿈
        count = 0
        flag = 0

        for i in range(len(p)):
            if p[i] == 'R':
                count += 1
            elif p[i] == 'D':
                # 종료조건 1
                if len(queue) < 1 or size == 0:
                    flag = 1
                    print("error")
                    break

                #앞과 뒤를 바꾼 상태에서 뒤에꺼를 제거 -> 앞에를 제거 하면 된다.
                if count % 2 != 0:
                    queue.pop()
                else:
                    queue.popleft()
        # for 문 다 돌았을때

        #error가 뜨면 flag = 1 로 종료되게 만들기 위해 이렇게 만듦
        if flag == 0:
            # 홀수이므로 reverse 할 필요 있음
            if count % 2 != 0:
                queue.reverse()

            print("[" + ",".join(queue) + "]") #이게 되내?

if __name__ == '__main__':
    main()