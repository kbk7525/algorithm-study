from math import factorial #factorial 사용 라이브러리
n,k = map(int, input().split())
a = factorial(n) // (factorial(k)*factorial(n-k)) #이항계수 공식
print(a)