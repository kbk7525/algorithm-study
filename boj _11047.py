n,k = map(int, input().split()) #동전의 종류와 동전으로 만들 돈의합 입력
money = []
cnt = 0

#오름차순으로 동전의 종류입력
for i in range(n):
    money.append(int(input()))

#역순(큰순서)으로 반복
for i in reversed(money):
    #만들돈이 0이면 반복종료
    if k == 0:
        break
    cnt += k // i #동전 갯수를 저장
    k %= i #나머지를 저장
print(cnt)