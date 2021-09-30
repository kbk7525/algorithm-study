#최솟값은 배열 하나를 내림차순으로 정렬하고 나머지를 오름차순으로 정렬해서
#a[0]*b[0]+..a[n-1]*b[n-1] 이런식으로 더해주면 된다

n = int(input()) #배열의 길이
a = list(map(int, input().split())) #배열 a 입력
b = list(map(int, input().split())) #배열 b 입력
a.sort() #a를 오름차순으로 정렬
b.sort(reverse=True) #b를 내림차순으로 정렬
s = 0 
for i in range(n):
    s += a[i]*b[i] #두 배열의 곱한값을 더해줌
print(s)