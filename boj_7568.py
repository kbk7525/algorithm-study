n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in arr:
    rank = 1
    for j in arr:
        #키랑 몸무게 비교해서 i가 더 작으면 rank 1증가
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')