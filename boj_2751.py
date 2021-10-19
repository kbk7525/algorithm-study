#Python3로 제출하면 시간초과가 나서 pypy3로 제출함
n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
for i in sorted(m):
    print(i)