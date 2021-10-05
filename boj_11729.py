#하노이탑 재귀함수
def hanoi(n,a,b,c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1,a,c,b)
        print(a, c)
        hanoi(n-1,b,a,c)

n = int(input())
print(2**n-1) #원판을 옮긴 횟수
hanoi(n,1,2,3)