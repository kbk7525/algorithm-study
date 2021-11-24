s = int(input())
n = 1
sum = 0 
#합이 s보다 작을때까지 반복
while sum <= s:
    sum += n
    n += 1
    #반복중에 합이 s보다 커질때 n-1해주고 반복종료
    if sum > s:
        n -= 1
        break
print(n-1)