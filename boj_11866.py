from collections import deque
n,k = map(int, input().split())
queue = deque()
arr = []
for i in range(1, n+1):
    queue.append(i)
while len(queue) > 0:
    for i in range(k-1):
        queue.append(queue.popleft())
    arr.append(queue.popleft())
print('<', end='')
print(*arr, sep=', ', end='')
print('>')