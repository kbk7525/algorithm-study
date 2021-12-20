#처음 이중포문으로 풀었더니 시간초과
#구글링하다가 제곱근을 이용해서 푼 블로그를 참고해서 풀었음
def sosu(num):
    #1은 소수가 아니므로 false
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            #num이 제곱근으로 나눠지면 false
            if num%i==0:
                return False
        return True
m,n=map(int, input().split())
arr=[]
for i in range(m, n+1):
    if sosu(i):
        print(i)