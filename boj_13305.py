n = int(input()) #도시 수
dst = list(map(int, input().split())) #두 도시를 연결하는 도로길이
price = list(map(int, input().split())) #도시의 기름 가격
minp = price[0] #기름값중의 최솟값
total = 0 #최소비용
#도착지는 빼고 그 사이에 기름값의 최솟값을 찾는과정
for i in range(n-1):
    if minp >= price[i]:
        minp = price[i]
    total += (dst[i]*minp) #최소 기름값과 거리를 곱해서 더함
print(total)