#처음에 리스트로 풀었더니 시간초과가 나서 집합으로 문제해결함
import sys
n,m = map(int, sys.stdin.readline().split())
li = set()
see = set()
#.strip()을 안해서 공백문자까지 리스트에 들어가 출력형식오류가 남
for _ in range(n):
    li.add(sys.stdin.readline().strip())
for _ in range(m):
    see.add(sys.stdin.readline().strip())
tmp = list(li & see) #교집합
tmp.sort()
print(len(tmp))
for i in tmp:
    print(i)