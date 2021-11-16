from collections import deque
queue = deque() #1부터 n까지 수를 넣을 큐
stack = [] #k번째 제거된 수를 저장할 스택
n,k=map(int, input().split())
for i in range(1,n+1):
    queue.append(i)
while len(queue) > 0:
    #큐에 k-1번째 수까지 팝해서 큐에 다시 넣음
    for i in range(k-1):
        queue.append(queue.popleft())
    #k번째 수를 팝해서 스택에 푸시
    stack.append(queue.popleft())
print('<', end='')
print(*stack, sep=', ', end='')
print('>')