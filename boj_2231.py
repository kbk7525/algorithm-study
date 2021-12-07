n = int(input())
m = 0
#n까지 전부 돌아봄
for i in range(n+1):
    #자릿수별로 잘라서 배열에 저장
    arr = list(map(int, str(i)))
    #원래 수와 자리수의 합
    s = i + sum(arr)
    #s와 n이 같으면 i가 생성자가 됨
    if s == n:
        m = i
        break
print(m)