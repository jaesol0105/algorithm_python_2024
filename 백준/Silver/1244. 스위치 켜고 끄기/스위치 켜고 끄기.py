# 2024-01-24 20:29

import sys
imput = sys.stdin.readline

N = int(input())
sw_list = [-1] + list(map(int,input().split()))
num_of_st = int(input())

for _ in range(num_of_st):
  sex, sw = map(int, input().split())
  
  if sex == 1: #남자
    for i in range(sw,N+1,sw):
      sw_list[i] = 0 if sw_list[i] == 1 else 1
      
  else: #여자
    sw_list[sw] = 0 if sw_list[sw] == 1 else 1
    k = 1
    while sw-k > 0 and sw+k <= N:
      if sw_list[sw-k] == sw_list[sw+k]:
        sw_list[sw-k] = 0 if sw_list[sw-k] == 1 else 1
        sw_list[sw+k] = 0 if sw_list[sw+k] == 1 else 1
        k += 1
      else:
        break

for i in range(1,N+1):
  print(sw_list[i], end=' ')
  if i % 20 == 0 :
    print()
    
'''
N = int(input())
sw_list = list(map(int,input().split()))
num_of_st = int(input())

for i in range(num_of_st):
  sex, sw = input().strip().split()
  sex, sw = int(sex), int(sw)
  
  if sex == 1: #남자
    origin_sw = sw
    while sw <= N:
      sw_list[sw-1] = 0 if sw_list[sw-1] == 1 else 1
      sw += origin_sw
      
  else: #여자
    sw_list[sw-1] = 0 if sw_list[sw-1] == 1 else 1
    neighbor = 1
    while sw-neighbor > 0 and sw+neighbor <= N:
      if sw_list[sw-neighbor-1] == sw_list[sw+neighbor-1]:
        sw_list[sw-neighbor-1] = 0 if sw_list[sw-neighbor-1] == 1 else 1
        sw_list[sw+neighbor-1] = 0 if sw_list[sw+neighbor-1] == 1 else 1
        neighbor += 1
      else:
        break

for i in range(1,N+1):
  if i % 20 == 0 :
    print(sw_list[i-1])
  else:
    print(sw_list[i-1], end=' ')
'''
