def NM(num):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(num, n+1):
        arr.append(i)
        NM(i)
        arr.pop()
n,m=map(int, input().split())
arr = []
NM(1)