#괄호의 짝이 맞는지 아닌지 판단하기 위해 stack 사용
t = int(input())
for _ in range(t):
    vps = input()
    stack = []
    for i in vps:
        #문자열이 '('이면 스택에 푸시 
        if i == '(':
            stack.append(i)
        #문자열이 ')'일 경우
        elif i == ')':
            #스택이 비지 않았고 '('가 있을경우 팝
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            #스택이 비었을때는 ')'푸시
            else:
                stack.append(i)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")