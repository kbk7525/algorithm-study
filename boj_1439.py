s=input()
cnt=0 #뒤집는 최소횟수
for i in range(len(s)-1):
    #문자열이 같지 않으면 횟수 1증가
    if s[i] != s[i+1]:
        cnt += 1
#위의 방법으로 하면 숫자가 바뀔때 2번씩 카운트되므로 2로 나눠줌
cnt = (cnt+1)//2
print(cnt)