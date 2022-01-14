# 처음에 이분탐색 알고리즘으로 풀고 답이 나와서 해보니 시간초과가 남
#구글링 해서 이분탐색대신 딕셔너리를 사용해 푸니 맞음
n = int(input())
card = list(map(int, input().split()))
card.sort()
m = int(input())
num = list(map(int, input().split()))
dic = dict()
for i in  card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in range(m):
    if num [i] in dic:
        print(dic[num[i]], end=' ')
    else:
        print(0, end=' ')