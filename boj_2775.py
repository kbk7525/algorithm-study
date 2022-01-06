t = int(input())
for _ in range(t):
    k = int(input()) #층
    n = int(input()) #호
    people = [[0 for i in range(n)]for i in range(k+1)] #층과 호수를 2차원배열로 표현
    #0층의 사람수
    for i in range(n):
        people[0][i] = i+1
    #1층부터 k층까지 사람수
    for i in range(1, k+1):
        for j in range(n):
            #아래층의 사람수를 더한 합을 배열에 넣어줌
            people[i][j] += sum(people[i-1][:j+1])
    print(people[k][n-1])