#2579번 계단오르기와 유사한 문제 (이 문제는  마지막을 포함 안해도 됨)
n = int(input())
arr = [0]*(n+2)
dp = [0]*(n+2)
for i in range(n):
    arr[i] = int(input())
dp[0] = arr[0]
dp[1] = arr[0]+arr[1]
#3번째 잔을 먹을때 첫번째,두번째의 합과 두번째,세번째의 합
#그리고 두번째 잔만 먹는 경우중 큰값을 골라 dp[2]에 넣음
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2], dp[1])
#마자막 잔의 전의 것을 먹은것과 전전의 것을 먹은경우,
#마지막 잔을 안먹은 경우 중 큰 것을 dp[i]에 (이거 때문에 틀림)
for i in range(3, n):
    dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i], dp[i-1])
print(dp[n-1])