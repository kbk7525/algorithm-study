n = int(input())
xy= []
#좌표들을 리스트형태로 리스트에 넣기
for i in range(n):
    xy.append(list(map(int, input().split())))
xy.sort() #정렬
for i in xy:
    print(i[0], i[1])