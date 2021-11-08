#시간초과 때문에 pypy3로 제출
#이진탐색으로 해결
n,m = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = max(arr)
res = 0
while start <= end:
    mid = (start+end)//2
    total = 0
    for i in arr:
        if i > mid:
            total += i-mid
    if total < m:
        end = mid-1
    else:
        res = mid
        start = mid+1
print(res)