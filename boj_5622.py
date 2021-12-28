#내가 푼 코드 if-else로 풀었는데 맞긴맞았다(살짝 비효율적인 느낌)
n = input()
t = 0
for i in n:
    if i=='A'or i=='B'or i=='C':
        t += 3
    elif i=='D'or i=='E'or i=='F':
        t += 4
    elif i=='G'or i=='H'or i=='I':
        t += 5
    elif i=='J'or i=='K'or i=='L':
        t += 6
    elif i=='M'or i=='N'or i=='O':
        t += 7
    elif i=='P'or i=='Q'or i=='R'or i=='S':
        t += 8
    elif i=='T'or i=='U'or i=='V':
        t += 9
    else:
        t += 10
print(t)
#다른 분의 코드 (이게 더 코드도 짧고 시간차이도 얼마 안난다)
#arr = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
#n = input()
#t = 0
#for i in n:
#    for j in arr:
#        if i in j:
#           t += arr.index(j)+3
#print(t)