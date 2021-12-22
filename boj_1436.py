n = int(input())
num = 666
cnt = 0
while True:
    #num에 666이 들어가있는지 확인 있으면 cnt+=1
    if '666' in str(num):
       cnt += 1
    #cnt와 n이 같으면 num 출력
    if cnt == n:
        print(num)
        break
    #666이 포함된 수가 나올때까지 1씩 증가
    num += 1 