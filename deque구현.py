from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    command = list(sys.stdin.readline().split())

    #정수 X를 덱의 앞에 넣는다.
    if command[0] == 'push_front':
        x = int(command[1])
        queue.appendleft(x)
    #정수 X를 덱의 뒤에 넣는다.
    elif command[0] == 'push_back':
        x = int(command[1])
        queue.append(x)
    #덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우 -1을 출력한다.
    elif command[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    #덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우  -1을 출력한다.
    elif command[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
#덱에 들어있는 정수의 개수를 출력한다.
    elif command[0] == 'size':
        print(len(queue))
#덱이 비어있으면 1을, 아니면 0을 출력한다.
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else :
            print(0)
#덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한
    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
#덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한
    elif command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

