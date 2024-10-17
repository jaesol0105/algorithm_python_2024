from collections import deque

N = int(input())

data= deque([i for i in range(1,N+1)])
cnt=1

while True:
    if len(data) == 1:
        print(data[0])
        break
    num = data.popleft()
    if cnt%2==0:
        data.append(num)
    cnt += 1