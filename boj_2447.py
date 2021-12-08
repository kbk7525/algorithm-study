#고민을 해봤지만 풀이하는것이 생각나지 않아서 블로그를 참조했다
#출처: https://leeiopd.tistory.com/297 

#재귀를 위한 함수
def star():
    l = len(arr)
    stars = [] #빈 배열
    for i in range(l*3):
        #공백을 찍는 방법
        if i // l == 1:
            stars.append(arr[i%l] + " " *l + arr[i%l])
        else:
            stars.append(arr[i%l]*3)
    return stars
n = int(input())
#별찍는 모양을 배열에 저장
arr = ["***", "* *", "***"]
cnt = 0
while n > 3:
    n //= 3
    cnt += 1
for i in range(cnt):
    arr = star()
for i in arr:
    print(i)