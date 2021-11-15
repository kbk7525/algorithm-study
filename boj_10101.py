a = int(input())
b = int(input())
c = int(input())
#세 각의 크기가 모두 60인 경우
if a==b==c==60:
    print("Equilateral")
#세 각의 합이 180이고, 두 각이 같은 경우
elif a+b+c==180 and (a==b or b==c or c==a):
    print("Isosceles")
#세 각의 합이 180이고, 같은 각이 없는 경우
elif a+b+c==180 and (a!=b!=c):
    print("Scalene")
#세 각의 합이 180이 아닌 경우
elif a+b+c!=180:
    print("Error")