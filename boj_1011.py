#처음에 문제를 잘못 이해해서 마지막만 1이 되면 되는줄 알았다
#실패해서 구글링해보니 도착하기 전에 광년이 계속 줄어야된다는 것을 알았다
t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    cnt = 0 #작동 횟수
    move = 0 #광년
    m = 1 #광년이 늘어나는 것
    dist = y-x #둘 사이의 거리
    while move < dist:
        move += m
        cnt += 1
        if cnt%2==0: #횟수가 2로 나눠지면 m에 1더함
            m += 1 
    print(cnt)