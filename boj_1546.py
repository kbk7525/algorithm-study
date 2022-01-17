n = int(input())
score = list(map(int, input().split()))
m = max(score)
s = 0
for i in range(n):
    score[i] = score[i]/m*100
print('%.2f' %(sum(score)/n))