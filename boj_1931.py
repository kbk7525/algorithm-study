n = int(input())
arr = [] #회의 시작시간과 끝나는시간을 저장하는 배열
cnt = 0
start = 0 #시작시간
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key=lambda a: a[0]) #시작시간을 기준으로 정렬
arr = sorted(arr, key=lambda a: a[1]) #위에서 정렬한것에서 끝나는시간을 오름차순으로 정렬
for i in range(n):
    if arr[i][0] >= start:
        start = arr[i][1] #시작시간을 해당 회의의 끝나는시간으로 바꿈
        cnt += 1
print(cnt)