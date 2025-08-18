from collections import deque

n,m = list(map(int, input().split())) #행 열
maps = []
result = [[-1]*m for _ in range(n)]
for r in range(n): #ryn
    maps.append(list(map(int, input().split())))

for r  in range(n): 
    for c in range(m):
        if maps[r][c] == 0:
            result[r][c] = 0
        if maps[r][c] == 2:
            result[r][c] = 0
            x,y = c, r

dx = [-1,0,1,0]
dy = [0,-1,0,1]

q = deque([(x,y)])

while q:
    x, y = q.popleft()
    d = result[y][x]

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if nx >=0 and ny >=0 and nx<m and ny<n:
            if result[ny][nx] == -1:
                result[ny][nx] = d+1
                q.append((nx,ny))

for r in range(n):
    print(' '.join(map(str, result[r])))