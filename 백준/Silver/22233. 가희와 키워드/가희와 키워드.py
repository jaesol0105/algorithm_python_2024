import sys
input = sys.stdin.readline

N,M = list(map(int, input().split()))

memo = set()
for _ in range(N):
    memo.add(input().strip())

for _ in range(M):
    keywords = input().strip().split(',')
    for word in keywords:
        if word in memo:
            memo.remove(word)
    print(len(memo))