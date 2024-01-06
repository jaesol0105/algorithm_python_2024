# 2024-01-07-00:48
import sys
input = sys.stdin.readline

p = int(input())

for _ in range(p): #1000
  child_list = list(map(int,input().split()))
  line = []
  cnt = 0
  for child in child_list[1:]: #20
    for child_in_line in line: #20
      if child_in_line > child:
        cnt += 1
    line.append(child)
  print(child_list[0],cnt)