n = int(input())
for i in range(1, n+1):
    #공백을 먼저 찍고 그 다음에 별 출력
    print(' '*(n-i) + '*'*i)