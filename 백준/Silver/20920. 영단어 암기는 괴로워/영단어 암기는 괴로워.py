from collections import defaultdict

N,M = list(map(int, input().split()))
cnt_dict = defaultdict(int)

for _ in range(N):
    word = input()
    if len(word) >= M:
        cnt_dict[word] += 1

result = sorted([[k,v] for k, v in cnt_dict.items()], key = lambda x:(-x[1],-len(x[0]),x[0]))

for k,v in result:
    print(k)