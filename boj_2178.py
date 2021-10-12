from collections import deque
#너비우선탐색 알고리즘으로 최소칸수 찾기
def miro(x,y):
    queue = deque()
    queue.append((x,y))
    #큐가 빌때까지 반복
    while queue:
        x,y = queue.popleft()
        #현재위치에서 방향확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #범위를 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #벽인 경우
            if graph[nx][ny] == 0:
                continue
            #처음 방문하는경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny)) 
    return graph[n-1][m-1] #최단거리 리턴

n,m = map(int, input().split()) 
graph = []
#이동할 네방향(상하좌우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#미로 입력
for i in range(n):
    graph.append(list(map(int, input())))
print(miro(0,0))