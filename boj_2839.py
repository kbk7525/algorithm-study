n = int(input()) #설탕 N kg 입력
cnt = 0 #봉지 갯수
while n >= 0: 
    if n % 5 == 0: #5의 배수일때
        cnt += n // 5 #5kg 봉지로 나눈 몫을 구해서 추가함
        print(cnt)
        break
    n -= 3 #5의 배수를 만들기위해 3씩 빼줌
    cnt += 1 #봉지 1개 추가
# 3kg과 5kg 봉지로 나눌수 없는경우 -1출력
else:
    print(-1)     