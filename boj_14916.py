n = int(input())
cnt = 0
while True:
    #5원짜리로 거스름돈 주는 경우
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    #2원짜리로 거스름돈 주는 경우(5로 나누기 위해 -2씩 해줌)
    else:
        n -= 2
        cnt += 1
    #거슬러 줄수 없는 경우
    if n < 0:
        print(-1)
        break