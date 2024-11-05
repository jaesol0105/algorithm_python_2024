import sys, heapq
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    for n in list(map(int,input().split())):
        if len(hq) < N:
            heapq.heappush(hq, n)
        elif hq[0] < n:
            heapq.heappop(hq)
            heapq.heappush(hq, n)
print(heapq.heappop(hq))