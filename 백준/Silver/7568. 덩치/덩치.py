# 2024-01-10 18:30
import sys
input = sys.stdin.readline

N = int(input())
info = [list(map(int,input().split())) for _ in range(N)]

cnt_of_bigger = []

for i in range(N):
  cnt = 1
  for j in range(N):
    if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
      cnt += 1
  print(cnt, end=' ')