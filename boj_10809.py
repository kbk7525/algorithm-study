s = input()
alpha ='abcdefghijklmnopqrstuvwxyz'
for i in alpha:
    if i in s: #문자열안에 알파벳이 있으면 해당 인덱스 번호의 숫자를 출력
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ') #나머지는 -1