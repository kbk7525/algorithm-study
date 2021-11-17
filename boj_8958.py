n = int(input())
for _ in range(n):
    score = 0
    tmp = 1 #누적합을 위한 변수
    s = input()
    for i in s:
        if i == 'O':
            score += tmp
            tmp += 1 #tmp 1증가
        #X일 경우 tmp를 다시 1로 초기화
        else:
            tmp = 1
    print(score)