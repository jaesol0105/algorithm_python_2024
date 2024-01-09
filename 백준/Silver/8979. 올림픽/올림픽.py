# 2024-01-09 11:30
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
rank = []
for _ in range(n):
  nation,g,s,b = map(int,input().split())
  rank.append([g,s,b,nation])

rank = sorted(rank, reverse=True, key = lambda x:(x[0],x[1],x[2]))

tmp = [0, rank[0][0:3]]
for i in range(1,n):
  if rank[i][3] == k:
    print(tmp[0]+1)
  if tmp[1] != rank[i][0:3]:
    tmp = [i, rank[i][0:3]]