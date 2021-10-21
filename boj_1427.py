n = input()
li = []
res = '' #내림차순으로 정렬한 결과값
for i in n:
    li.append(i)
li.sort(reverse=True) #내림차순으로 정렬
for i in li:
    res += i
print(res)