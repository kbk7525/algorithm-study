i = 0
while True:
    l, p, v = map(int, input().split())
    i += 1
    #모두 0을 입력하면 반복종료
    if l==0 and p==0 and v==0:
        break
    day = v//p #휴가중에 L일 동안 꽉채워서 사용할수있는 개수 
    reminder = v%p #나머지
    print("Case %d: %d" %(i, l*day+min(reminder, l))) #나머지와 L일중 작은것을 더함