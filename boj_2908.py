a,b=input().split()
#숫자를 역순으로 바꿔줌
a = int(a[::-1])
b = int(b[::-1])
#둘중 큰거 출력
print(max(a,b))