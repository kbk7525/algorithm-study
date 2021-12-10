#1시간 고민후 안풀려서 구글링을 했음
n = int(input())
arr = list(map(int, input().split()))
stack = []
res = [-1]*n #결과값
for i in range(n):
    #스택이 비지 않고 다음수가 현재 수보다 크면
    while len(stack)!=0 and arr[stack[-1]] < arr[i]:
        res[stack.pop()] = arr[i] #결과값 인덱스에 다음수를 넣음
    stack.append(i)
for i in res:
    print(i, end=' ')