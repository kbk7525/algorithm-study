#전에 풀었던 n과 m(1) 문제에서 함수 매개변수만 넣어서 풀었음
#다른점은 수열의 앞에 숫자보다 작거나 같은수가 오면 안되므로
#재귀를 할때 +1씩 해주었음
def NM(num):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(num, n+1):
        if i in arr:
            continue
        arr.append(i)
        NM(i+1)
        arr.pop()
n,m=map(int, input().split())
arr = []
NM(1)