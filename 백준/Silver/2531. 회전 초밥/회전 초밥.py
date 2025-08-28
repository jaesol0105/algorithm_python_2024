# 19:30 시작
# 연속 k 개 를 먹는다
# 종류의 최대값 : 쿠폰을 포함하지 않는, 중복없는 연속 k 개

# 최대 NlogN
# 마지막에 k-1 만큼 이어 붙이고 순회
# 현재 위치에서의 k개 set 했을때 길이기록, 이때 set에 보너스 포함 안되있어야함(어차피 주니까)
# 맥스갱신

import sys
input = sys.stdin.readline

N, d, k, c = list(map(int,input().split()))

data = [int(input()) for _ in range(N)]

for i in range(k-1):
    data.append(data[i])

ans = 0
for i in range(len(data)):
    s = set(data[i:i+k])
    if c not in s:
        ans = max(len(s)+1, ans)
    else:
        ans = max(len(s), ans)

print(ans)