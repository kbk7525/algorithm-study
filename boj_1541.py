n = input().split('-') #-를 기준으로 n을 쪼갬
arr = []
for i in n:
    res = 0
    #+로 묶인원소를 +를 기준으로 쪼개고 값을 더함
    s = i.split('+')
    for j in s:
        res += int(j)
    arr.append(res) #더한값들을 배열에 저장
num = arr[0] #첫번째 원소
#첫번째 원소를 제외하고 나머지 +로 묶였던 원소들의 합을 빼줌
for i in arr[1:]:
    num -= i
print(num)