#n과 m(1)문제풀이에서 수열에 자기자신이 있는지 확인하는 부분을 빼서 해결
def NM():
    if len(arr) == m:
        print(*arr)
        return
    for i in range(1, n+1):
        arr.append(i)
        NM()
        arr.pop()
n,m=map(int, input().split())
arr = []
NM()