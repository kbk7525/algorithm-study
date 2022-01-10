import sys
sudo = [] #스도쿠 보드판
blank = [] #스도쿠에서 빈칸으로 남겨진 x,y좌표를 저장하는 배열
#스도쿠의 행을 확인하는 함수
def row(x, n):
    #행에 이미 n이 있는경우 false
    for i in range(9):
        if n == sudo[x][i]:
            return False
    return True
#스도쿠의 열을 확인하는 함수
def col(y, n):
    #열에 이미 n이 있는경우 false
    for i in range(9):
        if n == sudo[i][y]:
            return False
    return True
#3*3 배열을 확인하는 함수
def squr(x,y,n):
    nx = x//3*3
    ny = y//3*3
    #3*3배열안에 이미 n이 있는 경우 false
    for i in range(3):
        for j in range(3):
            if n == sudo[nx+i][ny+j]:
                return False
    return True
#dfs를 수행하는 함수
def dfs(n):
    #blank배열이 비면 스도쿠 출력
    if n == len(blank):
        for i in range(9):
            print(*sudo[i])
        exit(0)
    for i in range(1, 10):
        x = blank[n][0]
        y = blank[n][1]
        if row(x,i) and col(y,i) and squr(x,y,i):
            sudo[x][y] = i
            dfs(n+1)
            sudo[x][y] = 0
for _ in range(9):
    sudo.append(list(map(int, sys.stdin.readline().rstrip().split())))
#스도쿠 배열을 돌면서 0이 있을때 blank배열에 x,y 좌표를 추가
for i in range(9):
    for j in range(9):
        if sudo[i][j] == 0:
            blank.append((i,j))
dfs(0)