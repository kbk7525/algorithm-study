#시간 초과때문에 sys.stdin.readline사용
import sys
#큐를 구현하기 위한 deque 라이브러리
from collections import deque
queue = deque()
n = int(sys.stdin.readline())
for i in range(n):
    order = sys.stdin.readline().split()
    #문제 구현 부분
    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])