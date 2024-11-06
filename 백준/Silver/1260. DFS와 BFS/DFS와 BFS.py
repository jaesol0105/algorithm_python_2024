import sys
input = sys.stdin.readline
from collections import deque

def dfs(v1):
    print(v1, end=' ')
    visited[v1] = 1
    for v2 in sorted(graph[v1]):
        if visited[v2] == 0:
            dfs(v2)

def bfs():
    while q:
        v1 = q.popleft()
        print(v1, end=' ')
        for v2 in sorted(graph[v1]):
            if visited[v2] == 0:
                visited[v2] = 1 #위치
                q.append(v2)

N,M,V = list(map(int,input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a) #양방향

q = deque([V])
visited = [0] * (N+1)
dfs(V)

print('')

q = deque([V])
visited = [0] * (N+1)
visited[V] = 1
bfs()
