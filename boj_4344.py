c=int(input())
for _ in range(c):
    score = list(map(int, input().split()))
    avg = sum(score[1:])/score[0]
    cnt = 0
    for i in score[1:]:
        if i > avg:
            cnt += 1
    rate = cnt/score[0]*100 #평균을 넘는 학생의 비율계산
    print('%.3f' %rate + '%')