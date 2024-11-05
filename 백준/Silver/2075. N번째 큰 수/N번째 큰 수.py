import sys, heapq
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    nums = list(map(int, input().split()))
    if not hq:
        for n in nums:
            heapq.heappush(hq, n)
    else:
        for n in nums:
            if hq[0] < n:
                heapq.heappush(hq, n)
                heapq.heappop(hq)
                
print(heapq.heappop(hq))