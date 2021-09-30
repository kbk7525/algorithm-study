n = 1000-int(input()) #1000엔을 냈을때 거스름돈
money = [500,100,50,10,5,1] #잔돈
cnt = 0 #잔돈의 갯수
for i in money: 
    cnt += n // i #거스름돈을 잔돈으로 나눈 몫을 갯수로 추가
    n %= i #나머지
print(cnt)