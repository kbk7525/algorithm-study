n = int(input())
t = list(map(int, input().split())) #묘목이 자라는 일수
t.sort(reverse=True) #내림차순으로 정렬
for i in range(n):
    t[i] = t[i]+i+1 #자라는 일수와 심는 순서, 심는데 걸리는시간 1일을 더해 배열에 저장
print(max(t)+1) #배열에서 가장큰값에 다자란 다음날을 더해 출력