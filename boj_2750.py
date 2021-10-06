#n개의 수를 입력받아 오름차순으로 정렬
n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
num.sort()
for i in num:
    print(i)