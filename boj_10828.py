#시간 초과때문에 sys.stdin.readline사용
import sys
stack = []
n = int(sys.stdin.readline())
for i in range(n):
    order = sys.stdin.readline().split()
    #문제 구현 부분
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])