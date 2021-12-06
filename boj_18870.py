#인덱스를 어떻게 접근할까 해서 구글링해보니 딕셔너리를 사용한것을 보았다
#딕셔너리를 이용해 문제해결
n = int(input())
x = list(map(int, input().split()))
arr = []
arr = list(set(x))
arr.sort()
dic = {arr[i]: i for i in range(len(arr))}
for i in x:
    print(dic[i], end=' ')