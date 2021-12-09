import sys
from collections import deque
queue = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    ord = sys.stdin.readline().split()
    if ord[0] == "push":
        queue.append(ord[1])
    elif ord[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif ord[0] == "size":
        print(len(queue))
    elif ord[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif ord[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif ord[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1]) 