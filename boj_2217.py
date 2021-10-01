n = int(input()) #n개의 로프
k = [] #로프의 최대중량을 저장하는 배열
for i in range(n):
    k.append(int(input()))
k.sort(reverse=True) #내림차순으로 정렬
a = [] #최대중량과 로프의 갯수의 곱을 저장할 배열
for i in range(n):
    a.append(k[i]*(i+1)) #곱을 배열에 추가
print(max(a)) #배열에서 가장 큰값을 출력