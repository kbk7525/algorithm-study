from collections import deque #bfs알고리즘에 필요한 deque 라이브러리

#깊이우선탐색 알고리즘
def dfs(graph, v, vistied):
    visited[v] = True #현재 정점 방문처리
    print(v, end=' ')
    #정점에 연결된 노드들을 탐색
    for i in graph[v]: 
        if not visited[i]: #방문처리 안되있으면
            dfs(graph, i, vistied) #재귀사용

#너비우선탐색 알고리즘
def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True #현재 정점 방문처리
    #큐가 빌떄까지 반복
    while queue:
        ver = queue.popleft() #큐에서 하나뽑음
        print(ver, end=' ')
        #정점에 연결된 노드들을 탐색
        for i in graph[ver]:
            if not visited[i]: #방문처리 안되있으면
                queue.append(i) #큐에 삽입
                visited[i] = True

n,m,v = map(int, input().split()) #정점, 간선, 탐색시작 정점번호
graph = [[] for _ in range(n+1)] 
for i in range(m):
    a,b = map(int, input().split()) #정점 입력
    #정점a별로 입력한 b를 추가(간선이 양방향이므로 b에서 a로 가는것도 추가)
    graph[a].append(b)
    graph[b].append(a)
    #오름차순으로 정렬
    graph[a].sort()
    graph[b].sort()

visited = [False]*(n+1) #false*m으로 하니 많은 정점중 간선하나인 경우 indexerror가 남
dfs(graph, v, visited)
print()

visited = [False]*(n+1)
bfs(graph, v, visited)