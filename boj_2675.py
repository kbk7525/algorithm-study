t = int(input()) #테스트케이스
for _ in range(t):
    r,s = map(str, input().split())
    r = int(r)
    #문자를 r번 반복
    for i in s:
        print(i*r, end='')
    print()