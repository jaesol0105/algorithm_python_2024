# 2024-01-05-22:30
import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
  cmd = input().strip()
  str, num = cmd.split() if ' ' in cmd else (cmd,-1)
  num = int(num)
  
  if str == 'add':
    s.add(num)
  elif str == 'remove' and num in s:
    s.remove(num)
  elif str == 'check':
    print(int(num in s))
  elif str == 'toggle':
    if num in s:
      s.remove(num)
    else:
      s.add(num)
  elif str == 'all':
    s = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
  else: # empty
    s = set()