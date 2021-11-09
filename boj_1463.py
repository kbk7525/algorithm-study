#다이나믹 프로그래밍으로 해결한 문제
n = int(input())
arr = [0]*(n+1)
for i in range(2, n+1):
    #1을 뺴는 경우
    arr[i] = arr[i-1]+1
    #3으로 나눠 떨어지는 경우
    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i//3]+1)
    #2로 나눠 떨어지는 경우
    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i//2]+1)
print(arr[n])