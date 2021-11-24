n = input()
arr = []
sum = 0
for i in n:
    arr.append(i)
#30의 배수가 되는 가장 큰수이므로 내림차순으로 정렬함
arr.sort(reverse=True)
#30의 배수가 되려면 자리수의 합이 3의 배수여야함
for i in arr:
    sum += int(i)
#30으로 나눠 떨어져야하므로 끝이 0이고 sum이 3으로 나눠떨어져야함
if arr[-1]=='0' and sum%3==0:
    for i in arr:
        print(i, end='')
else:
    print(-1)