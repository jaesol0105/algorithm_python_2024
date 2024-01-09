# 2024-01-09 11:30
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
rank = [list(map(int,input().split())) for _ in range(n)]
rank = sorted(rank, reverse=True, key = lambda x:(x[1],x[2],x[3]))

tmp_rank = 1
for i in range(n):
  if rank[i][0] == k: # 국가번호
    print(tmp_rank)
    break
  if rank[i][1:] != rank[i+1][1:]: # 공동 순위 고려
    tmp_rank = i+2 # 다음 등수 국가의 순위
