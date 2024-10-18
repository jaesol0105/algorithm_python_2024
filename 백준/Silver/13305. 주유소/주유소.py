import heapq

N= int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

hq = []
for idx, num in enumerate(price):
    heapq.heappush(hq,[num,idx])

result = 0
pointer = N

while hq:
    num, idx = heapq.heappop(hq)
    if pointer > idx and N-1 > idx:
        result += num * sum(distance[idx:pointer])
        pointer = idx

print(result)