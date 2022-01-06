#n이 h의 배수일 경우를 생각하지 못해서 틀렸다
t = int(input())
for _ in range(t):
    h,w,n=map(int, input().split())
    y = n%h
    x = n//h+1
    if n%h==0:
        y = h
        x = n//h
    print(y*100+x)