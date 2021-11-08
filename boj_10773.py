stack = []
k = int(input())
total = 0
for i in range(k):
    n = int(input())
    #0이면 pop
    if n == 0:
        stack.pop()
    #0이 아니면 push
    else:
        stack.append(n)
#스택이 비었으면 0
if len(stack) == 0:
    print(0)
#비지 않으면 스택의 원소 총합 출력
else:
    for i in stack:
        total += i
    print(total)