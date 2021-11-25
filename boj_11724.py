#처음에 recursionError가 나서 구글링해보니 setrecursionlimit으로
#재귀의 횟수를 바꿔줘야한다는것을 알았다
import sys
sys.setrecursionlimit(1000000)
#너비 우선 탐색 알고리즘
def bfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            bfs(graph, i, visited)

n,m=map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
cnt = 0 #연결요소의 갯수
for _ in range(m):
    a,b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
#정점을 돌면서 False인것이 있으면 갯수를 늘려주고 연결된 정점을 찾는다
for i in range(1, n+1):
    if visited[i] == False:
        cnt += 1
        bfs(graph, i, visited)
print(cnt)