import math
t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    #두 원의 중심사이의 거리
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    #두 원 사이의 거리가 0일 경우(원이 서로겹치는 경우)
    if dist == 0:
        #반지름이 같은경우(원이 겹침) 점점이 무수히 많으므로 -1출력
        if r1 == r2:
            print(-1)
        #원 안에 또다른 원이 들어가있는 경우 접점이 없으므로 0출력
        else:
            print(0)
    #원이 떨어져있는 경우(중심이 다름)
    else:
        #원이 둘이 닿아있는경우 점점은 1개이므로 1출력
        if (r1+r2 == dist or abs(r1-r2) == dist):
            print(1)
        #원이 둘이 겹쳐져있는 경우 접점은 2개이므로 2출력
        elif(r1+r2 > dist and abs(r1-r2) < dist):
            print(2)
        else:
            print(0)