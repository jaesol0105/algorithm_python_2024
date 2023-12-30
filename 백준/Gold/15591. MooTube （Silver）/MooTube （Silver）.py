import sys
from collections import deque
input = sys.stdin.readline

n, q = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  m1,m2,usado = map(int,input().split())
  graph[m1].append((m2,usado))
  graph[m2].append((m1,usado))

for _ in range(q):
  k, v = map(int, input().split())
  que = deque([(v, float("inf"))])
  visited = [0]*(n+1)
  visited[v] = 1
  count = 0
  while que:
    movie, usado = que.popleft()
    for next_movie, next_usado in graph[movie]:
      min_usado = min(next_usado,usado)
      if visited[next_movie] == 0 and min_usado >= k:
        que.append((next_movie, min_usado))
        visited[next_movie] = 1
        count += 1
  print(count)