#백트래킹이라는걸 잘몰라서 구글링하면서 문제해결
#재귀를 이용해 문제해결
def NM():
    #수열의 길이와 주어진 m과 같으면
    if len(arr) == m:
        print(*arr) #수열 출력
        return
    
    for i in range(1, n+1):
        #수열 안에 i가 포함되어 있으면 넘어감
        if i in arr:
            continue
        #없으면 i를 arr에 추가
        arr.append(i)
        NM()
        arr.pop()
n,m = map(int, input().split())
arr = [] #수열 출력을 위한 배열
NM()