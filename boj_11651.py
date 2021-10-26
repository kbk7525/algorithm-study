n = int(input())
xy = []
for _ in range(n):
    xy.append(list(map(int, input().split())))
xy.sort(key=lambda i : (i[1], i[0])) #y좌표 정렬후 같으면 x좌표 오름차순정렬 
for i in xy:
    print(i[0], i[1])