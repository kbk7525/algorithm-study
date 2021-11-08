#실패한이유: visited에 n+1이 아니라 n을 곱해서 인덱스에러가 났음
def dfs(graph, v, visited):
    global cnt #전역변수 설정
    visited[v] = True
    for i in graph[v]:
        if not visited[i]: #방문을 안했다면
            dfs(graph, i, visited) #재귀
            cnt += 1 #수를 1증가

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
p = int(input())
cnt = 0 #바이러스 걸리는 컴퓨터 수
for i in range(p):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(graph, 1, visited)
print(cnt)