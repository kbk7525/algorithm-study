#n이 3보다 클 경우 n-1, n-2, n-3번째 경우를
#더한값과 같다는 규칙을 찾아냈다
def plus(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return plus(n-1)+plus(n-2)+plus(n-3)
t = int(input())
for _ in range(t):
    n = int(input())
    print(plus(n))