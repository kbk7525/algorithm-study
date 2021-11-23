#다이나믹 프로그래밍으로 해결
n = int(input())
#arr에 0을 안넣고 풀었더니 인덱스에러가 남
arr = [0]*301
dp = [0]*301
for i in range(n):
    arr[i] = int(input())
dp[0] = arr[0]
dp[1] = arr[0]+arr[1]
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])
#도착점 전의 계단을 밟은경우와 전전 계단을 밟은경우중 큰 것을 dp[i]에 넣음
for i in range(3, n):
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
print(dp[n-1]) #계단이 0번부터 시작하므로 n-1번째를 출력