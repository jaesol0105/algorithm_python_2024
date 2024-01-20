# 2024-01-20 10:30

import sys
imput = sys.stdin.readline

N = int(input())

cookie = []
for i in range(N):
  cookie.append(input().strip())

dx=[-1,0,0,1,1,1] #머리,왼팔,오팔,허리,왼다,오다
dy=[0,-1,1,0,-1,1]
hx,hy= -1,-1
for i in range(1,N-1):
  for j in range(1,N-1):
    if [cookie[i+dx[k]][j+dy[k]] for k in range(4)] == ['*','*','*','*']:
      hx,hy = i,j
      print(str(hx+1)+' '+str(hy+1))

for k in range(1,6):
  cnt = 0
  x=hx+dx[k]
  y=hy+dy[k]
  while x>=0 and x<N and y>=0 and y<N:
    if cookie[x][y] != '*':
      break
    cnt+=1
    if k == 3:
      hx,hy = x,y
    if k > 3:
      x += 1
    else:
      x += dx[k]
      y += dy[k]
  print(cnt, end=' ')