#다이나믹 프로그래밍으로 해결 (생각보다 구현은 어렵지 않았음)
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
for i in range(1,n):
    #빨강색일경우 i-1번째에서 초록색,파랑색중 작은값을 고른후 더함
    arr[i][0] = min(arr[i-1][1], arr[i-1][2])+arr[i][0]
    #초록색일경우 i-1번째에서 빨강색,파랑색중 작은값을 고른후 더함
    arr[i][1] = min(arr[i-1][0], arr[i-1][2])+arr[i][1]
    #파랑색일경우 i-1번째에서 빨강색,초록색중 작은값을 고른후 더함
    arr[i][2] = min(arr[i-1][0], arr[i-1][1])+arr[i][2]
print(min(arr[n-1][0], arr[n-1][1], arr[n-1][2]))