# 2024-01-22 16:09

import sys
imput = sys.stdin.readline

N, score, P = map(int,input().split())
result = -1

if N != 0:
  full_list = list(map(int,input().split()))
  full_list = sorted(full_list, reverse=True)
  
  for i in range(N):
    if score >= full_list[i]: #i+1등
      result = i+1
      break

  if N == P and score == full_list[-1]: #랭킹 리스트 꽉차고, 이전 점수와 동점일 경우
    result = -1
  
if N < P and result == -1: #꼴등이지만 자리가있을경우
  result = N+1

print(result)
    
    
  