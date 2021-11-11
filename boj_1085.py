#x,y가 직사각형 안에 있기 때문에 4가지 경우 중 최솟값을 출력
x,y,w,h = map(int, input().split())
print(min(x,y,w-x,h-y))