#이진 탐색 알고리즘 (재귀)
def bs(arr, v, start, end):
    if start > end:
        return 0 #없으면 0
    mid = (start+end)//2
    if arr[mid] == v:
        return 1 #찾으면 1
    elif arr[mid] > v:
        return bs(arr, v, start, mid-1)
    else:
        return bs(arr, v, mid+1, end)

n = int(input())
num = list(map(int, input().split()))
num.sort() #오름차순으로 정렬
m = int(input())
a = list(map(int, input().split()))
#존재하는지 확인
for i in a:
    print(bs(num, i, 0, n-1))