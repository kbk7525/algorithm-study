n = input()
num_list = [0]*9 #9를 제외한 나머지 번호 리스트
for i in n:
    i = int(i)
    #9이면 6의 갯수 1증가
    if i == 9:
        num_list[6] += 1
    else:
        num_list[i] += 1
#2개씩 짝이 맞으면 2로 나눔
if num_list[6]%2==0:
    num_list[6] = num_list[6]//2
#짝이 안맞으면 2로 나눈후 1을 더함
else:
    num_list[6] = num_list[6]//2+1
print(max(num_list))