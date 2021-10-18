n = int(input())
cnt = 0 #사이클 길이
num = n
while True:
    a = num//10 #10의 자리
    b = num%10 #1의 자리
    c = (a+b)%10 #둘이 더해서 1의자리만 저장
    num = (b*10)+c #새로운 수
    cnt += 1 #사이클 증가
    #같은지 비교
    if num == n:
        break;
print(cnt)