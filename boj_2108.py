#이 문제 풀면서 most_common이라는 것을 알게 됨
import sys
from collections import Counter #최빈값을 구하는 most_common을 사용하기 위해
n = int(sys.stdin.readline())
a = []
for _ in range(n):
   a.append(int(sys.stdin.readline()))
a.sort()  
print(round(sum(a)/n)) #산술평균
print(a[n//2]) #중앙값
c = Counter(a).most_common(2) #최빈값 2개를 뽑음
#두수의 빈도수가 같은경우
if len(a) > 1 and c[0][1] == c[1][1]:
   print(c[1][0]) #두번째로 작은값 출력
#다른경우
else:
   print(c[0][0]) #가장 작은값 출력
print(max(a)-min(a)) #범위출력