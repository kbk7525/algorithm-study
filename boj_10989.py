#배열에 넣고 정렬하면 메모리초과가 뜸
#그래서 배열인덱스에 바로 넣는 방법으로 품

import sys #메모리 아끼기 위해 라이브러리 사용
n = int(input())
m = [0]*10001 #10000보다 작은수를 입력하므로 10001개의 배열을 생성
for i in range(n):
    num = int(sys.stdin.readline())
    m[num] += 1 #입력한 숫자에 대한 인덱스 1증가

#배열 출력 
for i in range(len(m)):
    for j in range(m[i]):
        print(i)