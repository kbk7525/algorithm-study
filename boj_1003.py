#다이나믹 프로그래밍으로 해결(일반 재귀로 하면 시간초과)
t = int(input())
zero = [1,0] #n이 0일때
one = [0,1] #n이 1일때
#n이 2이상일때 점화식으로 표현
for i in range(2, 41):
    zero.append(zero[i-1]+zero[i-2])
    one.append(one[i-1]+one[i-2])
for _ in range(t):
    n = int(input())
    print(zero[n], one[n]) 