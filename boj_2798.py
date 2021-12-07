n,m = map(int, input().split())
arr = list(map(int, input().split()))
s = 0 #가장 큰 합을 저장
#삼중 포문으로 3개의 경우의 수를 모두 돌려봄
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            #3개의 합이 m보다 클때는 넘어감
            if arr[i]+arr[j]+arr[k] > m:
                continue
            #작을때는 s와 3개의합 중 큰값을 s에 저장
            else:
                s = max(s, arr[i]+arr[j]+arr[k])
print(s)