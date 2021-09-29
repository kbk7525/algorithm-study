n = int(input()) #n명의 사람
t = list(map(int, input().split())) #걸리는 시간을 list로 저장
t.sort() #오름차순으로 정렬
s = 0 #누적시간
tmp = [] #누적시간을 저장할 배열
for i in t:
    s += i
    tmp.append(s) #배열에 저장
print(sum(tmp)) #누적시간을 모두 더한값을 출력