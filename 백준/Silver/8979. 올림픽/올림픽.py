# 2024-01-09 11:30
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
rank = []
for _ in range(n):
  nation,g,s,b = map(int,input().split())
  rank.append([g,s,b,nation])

rank = sorted(rank, reverse=True, key = lambda x:(x[0],x[1],x[2]))

tmp_rank = 1
for i in range(n):
  if rank[i][3] == k: # 국가번호
    print(tmp_rank)
    break
  if rank[i][0:3] != rank[i+1][0:3]:
    tmp_rank = i+2