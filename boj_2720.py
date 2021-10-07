t = int(input()) #테스트 케이스
c = [] #거스름돈
for i in range(t):
    c.append(int(input()))
#쿼터,다임,니켈,페니의 갯수를 출력
for i in range(len(c)):
    print(c[i] // 25, end = ' ')
    c[i] %= 25
    print(c[i] // 10, end = ' ')
    c[i] %= 10
    print(c[i] // 5, end = ' ')
    c[i] %= 5
    print(c[i] // 1)