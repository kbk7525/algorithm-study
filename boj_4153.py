while True:
    x,y,z = map(int, input().split())
    #모두 0이면 반복종료
    if x==0 and y==0 and z==0:
        break
    #두변의 제곱의 합이 한변의 제곱과 같으면 right 
    if (x**2)+(y**2)==(z**2) or (x**2)+(z**2)==(y**2) or (y**2)+(z**2)==(x**2):
        print("right")
    else:
        print("wrong")